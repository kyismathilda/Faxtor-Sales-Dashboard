import streamlit as st
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* Background */
.main {
    background-color: #f7f8fc;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #eef1fb;
    padding: 20px;
}

/* Sidebar menu */
div[role="radiogroup"] > label {
    background-color: #dbe2ff;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 500;
}

div[role="radiogroup"] > label:hover {
    background-color: #cfd7ff;
}

/* Metric card */
div[data-testid="metric-container"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* Progress bar */
.stProgress > div > div > div > div {
    background-color: #ff4b5c;
}

/* Title */
h1, h2, h3 {
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.image("logo_faxtor.png", width=1000)
    st.markdown("## Business Dashboard")

    page = st.radio(
        "Features",
        [
            "Revenue & Profit Tracker",
            "Expansion Tracker",
            "Royalty Calculator",
            "Sales Forecaster",
            "2026 Calendar"
        ]
    )

# =========================
# YOUR DATA
# =========================
royalty_pricing = {
    "PII": 45000,
    "OPTI": 40000,
    "MSSQ": 40000,
    "GWS": 45000,
    "INCRITS": 50000,
}

revenue_actual=2437661932
revenue_target=9000000000
profit_actual=755626322
profit_target=3600000000

expansion_data = {
    "Jawa":{"Banten":50,"DIY":16,"DKI Jakarta":158,"Jawa Barat":223,"Jawa Tengah":19,"Jawa Timur":32},
    "Sumatra":{"Aceh":7,"Bangka Belitung":2,"Jambi":2,"Kep. Riau":5,"Lampung":4,"Riau":4,"Sumatra Barat":7,"Sumatra Selatan":3,"Sumatra Utara":23},
    "Kalimantan":{"Kalimantan Barat":3,"Kalimantan Selatan":1,"Kalimantan Tengah":4,"Kalimantan Timur":8,"Kalimantan Utara":2},
    "Sulawesi":{"Sulawesi Tenggara":4,"Sulawesi Selatan":5},
    "BaliNusra":{"Bali":8,"NTB":2},
    "Papua":{"Jayapura":2,"Sorong":1},
}

image_map = {
    "Jawa":"Jawa.png",
    "Sumatra":"Sumatra.png",
    "Kalimantan":"Kalimantan.png",
    "Sulawesi":"Sulawesi.png",
    "BaliNusra":"Bali.png",
    "Papua":"Papua.png",
}

standard_pricing= {
    "BIG FIVE": 30000,"EII": 40000,"FCAT": 90000,"FCAT Short": 50000,"FEAST": 40000,
    "FMAT": 50000,"FTPI": 30000,"GWS": 45000,"IAMAR": 40000,"INCRITS": 50000,
    "LSSI": 20000,"MSSQ MSDQ": 40000,"OPTI": 50000,"PII": 45000,
    "Package 1 - Student Ultimate Assessment": 195000,
    "Package 2 - Complete Critical Thinking Assessment (OPTI Vers)": 215000,
    "Package 3 - Complete Critical Thinking Assessment": 190000,
    "Package 4 - High School Majoring Assessment": 175000,
    "Package 5 - Corporate Complete Assessment": 160000,
    "Package 6 - Career Mapping Assessment": 130000,
    "Package 7 - Corporate Complete Assessment Short Vers": 110000,
    "Package 8 - Middle School Selection Assessment": 95000,
    "Package 9 - Corporate Brief Assessment": 80000,
    "Package 10 - Middle School Selection Assessment Short Vers": 60000,
}

professional_pricing= {
    "BIG FIVE": 35000,"EII": 45000,"FCAT": 100000,"FCAT Short": 60000,"FEAST": 45000,
    "FMAT": 60000,"FTPI": 35000,"GWS": 50000,"IAMAR": 50000,"INCRITS": 55000,
    "LSSI": 25000,"MSSQ MSDQ": 45000,"OPTI": 60000,"PII": 50000,
    "Package 1 - Student Ultimate Assessment": 230000,
    "Package 2 - Complete Critical Thinking Assessment (OPTI Vers)": 250000,
    "Package 3 - Complete Critical Thinking Assessment": 220000,
    "Package 4 - High School Majoring Assessment": 205000,
    "Package 5 - Corporate Complete Assessment": 175000,
    "Package 6 - Career Mapping Assessment": 155000,
    "Package 7 - Corporate Complete Assessment Short Vers": 140000,
    "Package 8 - Middle School Selection Assessment": 110000,
    "Package 9 - Corporate Brief Assessment": 90000,
    "Package 10 - Middle School Selection Assessment Short Vers": 70000,
}

gross_target=750000000

logo_map = {
    "BIG FIVE": "BIGFIVE.png",
    "EII": "EII.png",
    "FCAT": "FCAT.png",
    "FCAT Short": "FCATS.png",
    "FEAST": "FEAST.png",
    "FMAT": "FMAT.png",
    "FTPI": "FTPI.png",
    "GWS": "GWS.png",
    "IAMAR": "IAMAR.png",
    "INCRITS": "INCRITS.png",
    "LSSI": "LSSI.png",
    "MSSQ MSDQ": "MSSQ.png",
    "OPTI": "OPTI.png",
    "PII": "PII.png",
}

# =========================
# PAGE 1
# =========================
if page == "Revenue & Profit Tracker":

    revenue_pct = (revenue_actual/revenue_target)*100
    profit_pct = (profit_actual/profit_target)*100

    st.title("Business Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue")
        st.metric("", f"Rp{revenue_actual:,}", f"{revenue_pct:.0f}% of target")

    with col2:
        st.subheader("Profit")
        st.metric("", f"Rp{profit_actual:,}", f"{profit_pct:.0f}% of target")

    st.subheader("Progress to Target")

    st.progress(revenue_pct/100)
    st.caption(f"{revenue_pct:.0f}%")

    st.progress(profit_pct/100)
    st.caption(f"{profit_pct:.0f}%")

# =========================
# PAGE 2
# =========================
elif page == "Expansion Tracker":

    st.title("Expansion Tracker")

    total_all = sum(sum(prov.values()) for prov in expansion_data.values())
    st.metric("Total Indonesia Client", total_all)

    for island in expansion_data:

        st.subheader(island)

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(image_map[island], width=700)

        with col2:
            table = pd.DataFrame(
                list(expansion_data[island].items()),
                columns=["Province", "Client"]
            )

            total_client = table["Client"].sum()
            percentage = (total_client/total_all)*100

            st.metric(f"{island} Client", total_client, f"{percentage:.0f}% of total")
            st.bar_chart(table.set_index("Province"))

# =========================
# PAGE 3
# =========================
elif page == "Royalty Calculator":

    st.title("Royalty Calculator")

    # =========================
    # MODE
    # =========================
    mode = st.radio("Skema Royalti", ["Percentage-based", "Fixed Number"])

    # =========================
    # DATAFRAME AWAL
    # =========================
    table = pd.DataFrame(
        list(royalty_pricing.items()),
        columns=["Product", "Price"]
    )

    # =========================
    # LOGIC ROYALTY
    # =========================
    if mode == "Percentage-based":
        rate = st.slider("Royalty Rate (%)", 0, 100, 30)
        rate = rate / 100

        table["Royalty"] = (table["Price"] * rate).astype(int)

    else:
        fixed = st.slider("Fixed Number (Rp)", 0, 50000, 10000)
        table["Royalty"] = fixed

    # =========================
    # TAMBAHAN
    # =========================
    table["Server Cost"] = 10000

    table["Margin (%)"] = (
        (table["Price"] - table["Royalty"] - table["Server Cost"])
        / table["Price"] * 100
    ).round(0).astype(int)

    # =========================
    # STYLING TABLE
    # =========================
    styled_table = table.style.set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#dbe2ff"),  # biru muda
                ("color", "#2c3e50"),
                ("font-weight", "bold")
            ]
        }
    ])

    # OPTIONAL FORMAT RUPIAH
    styled_table = styled_table.format({
        "Price": "Rp{:,.0f}",
        "Royalty": "Rp{:,.0f}",
        "Server Cost": "Rp{:,.0f}"
    })

    # =========================
    # OUTPUT
    # =========================
    st.subheader("Royalty Table")
    st.dataframe(styled_table)

# =========================
# PAGE 4

elif page == "Sales Forecaster":

    st.title("Sales Forecaster")

    # =========================
    # PILIH PRICING
    # =========================
    mode = st.radio(
        "Pilih Jenis Pricing",
        ["Standard Enterprise", "Professional Enterprise"]
    )

    pricing = standard_pricing if mode == "Standard Enterprise" else professional_pricing

    # =========================
    # TARGET
    # =========================
    st.metric("Monthly Gross Target", f"Rp{gross_target:,}")

    # =========================
    # LAYOUT
    # =========================
    col1, col2 = st.columns([1,1])

    quantity = {}
    data = []
    total_revenue = 0

    # =========================
    # INPUT AREA (KIRI)
    # =========================
    with col1:
        st.subheader("Volume Penjualan")

        for product in pricing:

            col_img, col_slider = st.columns([1,3])

            # === LOGO / TEXT ===
            with col_img:
                if product in logo_map:
                    st.image(logo_map[product], width=70)
                    st.caption(product)  # optional biar tetap kebaca
                else:
                    st.markdown(f"**{product}**")

            # === SLIDER ===
            with col_slider:
                quantity[product] = st.slider(
                    label="",
                    min_value=0,
                    max_value=50000,
                    value=0,
                    step=5,
                    key=product
                )

    # =========================
    # CALCULATION
    # =========================
    for product in pricing:
        price = pricing[product]
        qty = quantity[product]
        revenue = price * qty

        total_revenue += revenue

        data.append({
            "Product": product,
            "Price": price,
            "Quantity": qty,
            "Revenue": revenue
        })

    df = pd.DataFrame(data)
    achievement = (total_revenue / gross_target) * 100

    # =========================
    # OUTPUT AREA (KANAN)
    # =========================
    with col2:
        st.subheader("Total Revenue")

        st.metric(
            label="",
            value=f"Rp{total_revenue:,}",
            delta=f"{achievement:.0f}% of target"
        )

        st.bar_chart(df.set_index("Product")["Revenue"])

elif page == "Faxtor Calendar":

    st.title("Faxtor Calendar")

    # =========================
    # DATA
    # =========================
    events = {
        "April": [
            {"date": "15", "title": "April Newsletter “Love Bombing di Kantor”", "desc": "BA, Marcomm, R&D"},
            {"date": "18", "title": "Sumatra Webinar Series Vol 01 with APIO Sumatra Barat & APIO Lampung", "desc": "BA, Marcomm, R&D"},
            {"date": "25", "title": "[START] Program Diskon May Day", "desc": "BA, BS"},
        ],
        "May": [
            {"date": "4", "title": "[START] Assessment Center Training", "desc": "All Division"},
            {"date": "15", "title": "[START] Program Biro Juara", "desc": "BA & BS"},
            {"date": "15", "title": "May Newsletter “Syarat Rekrutmen IPK 3.0”, "desc": "BA, Marcomm, R&D"},
            {"date": "16", "title": "Sumatra Webinar Series Vol 02 with Discoverme”, "desc": "BA, Marcomm, PLES"},
            {"date": "30", "title": "Education Webinar with Asosiasi Psikolog Pendidikan Indonesia (APSI) DKI Jakarta”, "desc": "BA, Marcomm, PLES"},
        ]
        "June": [
            {"date": "15", "title": "May Newsletter “Cybernetic Leadership”, "desc": "BA, Marcomm, R&D"},
        ]
        "July": [
            {"date": "15", "title": "May Newsletter “Karyawan Penurut vs Pembangkang”, "desc": "BA, Marcomm, R&D"},
            {"date": "18", "title": "[TENTATIVE] Webinar with APIO Jawa Tengah”, "desc": "BA, Marcomm, R&D"},
    }

    # =========================
    # CUSTOM CSS
    # =========================
    st.markdown("""
        <style>
        .date-box {
            background-color: #f55164;
            color: white;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            border-radius: 8px;
        }

        .event-card {
            background-color: #e5e7eb;
            padding: 15px;
            border-radius: 8px;
        }

        .event-title {
            font-size: 18px;
            font-weight: 600;
            color: #2c3e50;
        }

        .event-desc {
            font-size: 14px;
            color: #6b7280;
        }
        </style>
    """, unsafe_allow_html=True)

    # =========================
    # LOOP EVENTS
    # =========================
    for month, month_events in events.items():

        st.subheader(month)

        for event in month_events:
            col1, col2 = st.columns([1, 5])

            with col1:
                st.markdown(f"""
                    <div class="date-box">
                        {event['date']}
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class="event-card">
                        <div class="event-title">{event['title']}</div>
                        <div class="event-desc">{event['desc']}</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
