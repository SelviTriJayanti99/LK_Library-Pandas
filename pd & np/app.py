from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    # Data Anime
    data = {
        "Judul": ["Naruto", "Attack on Titan", "My Hero Academia", "One Piece", "Demon Slayer"],
        "Genre": ["Action, Adventure", "Action, Fantasy", "Action, Superhero", "Adventure, Fantasy", "Action, Supernatural"],
        "Tahun Rilis": [2002, 2013, 2016, 1999, 2019],
        "Studio": ["Studio Pierrot", "WIT Studio", "Bones", "Toei Animation", "ufotable"]
    }
    df = pd.DataFrame(data)

    # Statistik dengan NumPy
    tahun_rilis = np.array(df["Tahun Rilis"])
    rata2 = np.mean(tahun_rilis)
    median = np.median(tahun_rilis)
    std_dev = np.std(tahun_rilis)
    cumulative = np.cumsum(tahun_rilis)

    # Convert DataFrame ke HTML table
    table_html = df.to_html(classes='data', index=False)

    return render_template ("index.html",
        table=table_html,
        rata2=rata2,
        median=median,
        std_dev=std_dev,
        cumulative=cumulative,
        )

if __name__ == '__main__':
    app.run(debug=True)
