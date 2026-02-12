import pandas as pd

# ======================================================
# BI RATE PREPROCESSING
# ======================================================
def preprocess_bi_rate(df_bi):
    """
    Preprocess BI-7Day Reverse Repo Rate data:
    - Convert Indonesian date string to datetime
    - Extract year & month
    - Convert BI rate to numeric
    """

    df = df_bi.copy()

    # standardize column names
    df.columns = [col.lower().strip() for col in df.columns]

    # rename for consistency
    df = df.rename(columns={
        "tanggal": "date",
        "bi-7day-rr": "bi_rate"
    })

    # ----------------------------------
    # HANDLE INDONESIAN MONTH NAMES
    # ----------------------------------
    month_map = {
        "januari": "01",
        "februari": "02",
        "maret": "03",
        "april": "04",
        "mei": "05",
        "juni": "06",
        "juli": "07",
        "agustus": "08",
        "september": "09",
        "oktober": "10",
        "november": "11",
        "desember": "12",
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "jun": "06",
        "jul": "07",
        "agu": "08",
        "sep": "09",
        "okt": "10",
        "nov": "11",
        "des": "12"
    }

    # convert date to lowercase string
    df["date"] = df["date"].astype(str).str.lower()

    # replace Indonesian month names with numbers
    for indo_month, num_month in month_map.items():
        df["date"] = df["date"].str.replace(
            indo_month, num_month, regex=False
        )

    # now parse datetime safely (format: DD MM YYYY)
    df["date"] = pd.to_datetime(df["date"], format="%d %m %Y")

    # extract year & month
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    # convert BI rate from percentage string to float
    df["bi_rate"] = (
        df["bi_rate"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .astype(float)
    )

    df = df[["year", "month", "bi_rate"]]

    return df

# ======================================================
# INFLATION PREPROCESSING
# ======================================================
def preprocess_inflation(df_inf):
    """
    Preprocess inflation data:
    - Handle Indonesian month names
    - Extract year & month robustly
    - Convert inflation to numeric
    """

    df = df_inf.copy()
    df.columns = [col.lower().strip() for col in df.columns]

    df = df.rename(columns={
        "periode": "period",
        "data inflasi": "inflation"
    })

    month_map = {
        "januari": "01",
        "februari": "02",
        "maret": "03",
        "april": "04",
        "mei": "05",
        "juni": "06",
        "juli": "07",
        "agustus": "08",
        "september": "09",
        "oktober": "10",
        "november": "11",
        "desember": "12",
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "jun": "06",
        "jul": "07",
        "agu": "08",
        "sep": "09",
        "okt": "10",
        "nov": "11",
        "des": "12"
    }

    df["period"] = df["period"].astype(str).str.lower()

    for indo_month, num_month in month_map.items():
        df["period"] = df["period"].str.replace(
            indo_month, num_month, regex=False
        )

    # sekarang format aman: MM-YYYY atau YYYY-MM
    df["date"] = pd.to_datetime(df["period"], errors="raise")

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    df["inflation"] = (
        df["inflation"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .astype(float)
    )

    return df[["year", "month", "inflation"]]

# ======================================================
# MERGE MACRO DATA
# ======================================================
def merge_macro_data(df_bi, df_inf):
    """
    Merge BI Rate & Inflation:
    - Inner join by year & month
    - Sort by time
    - Create YYYY-MM period
    """

    df = pd.merge(
        df_bi,
        df_inf,
        on=["year", "month"],
        how="inner"
    )

    # sort chronologically
    df = df.sort_values(["year", "month"])

    # reset index = official start of analysis pipeline
    df = df.reset_index(drop=True)

    # create period column
    df["period"] = (
        df["year"].astype(str) + "-" +
        df["month"].astype(str).str.zfill(2)
    )

    return df