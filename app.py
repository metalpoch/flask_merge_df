"""
Start Flask App
"""
import asyncio
from os import path

from flask import Flask, render_template, request, send_file, session
from werkzeug.utils import secure_filename

from src import dataframe, temporal_directory

app = Flask(__name__)
app.config["SECRET_KEY"] = "cachapa frita"
PATH = path.dirname(path.abspath(__file__))


@app.route("/", methods=["GET", "POST"])
async def index():
    if request.method == "POST":
        files = [request.files.get("file1"), request.files.get("file2")]
        separators = [request.form.get("sep1"), request.form.get("sep2")]
        if files[0].filename == '' or files[1].filename == '':
            return render_template("index.html")

        if session.get("data"):  # Remove old tmp_directory
            temporal_directory.remove(session["data"][0]["tmp_directory"])
            session.pop("data")

        tmp_directory = temporal_directory.create(PATH)

        data = []  # Index 0 == "file left". Index 1 == "file right"
        for file, sep in zip(files, separators):
            filename = secure_filename(file.filename)
            filepath = path.join(tmp_directory, filename)
            file.save(filepath)
            
            columns = await dataframe.get_columns(filepath, sep)
            data.append({
                "filepath": filepath,
                "tmp_directory": tmp_directory,
                "filename": filename,
                "columns": columns,
                "sep": sep
            })

        session["data"] = data
        
        return render_template(
            "index.html", data=data,
            columns_1=data[0]["columns"],
            columns_2=data[1]["columns"],
            filename_1=data[0]["filename"],
            filename_2=data[1]["filename"],
        )

    return render_template("index.html")


@app.route("/download", methods=["GET", "POST"])
async def download():
    if request.method == "POST":
        left_on = request.form.getlist("left_on")
        right_on = request.form.getlist("right_on")
        how = request.form.get("how")

        file_left = session["data"][0]["filepath"]
        file_right = session["data"][1]["filepath"]
        tmp_directory = session["data"][0]["tmp_directory"]
        out_file= path.join(tmp_directory, "merge.xlsx")
        sep_left = session["data"][0]["sep"]
        sep_right = session["data"][1]["sep"]

        await dataframe.merge(
            file_left=file_left,
            file_right=file_right,
            left_on=left_on,
            right_on=right_on,
            how=how,
            out_file=path.join(tmp_directory, "merge.xlsx"),
            sep_left=sep_left,
            sep_right=sep_right
        )

        return send_file(out_file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
