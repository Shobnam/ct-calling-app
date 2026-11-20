import streamlit as st
import psycopg2

st.set_page_config(
    page_title="CT Dashboard",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Today's Calling List - CT")
st.subheader("Database Connection Test")

# ==========================
# DATABASE DETAILS
# ==========================
DB_HOST = "pre-prod-py-postgresql14-reader-replica.postgres.database.azure.com"
DB_PORT = 5432
DB_NAME = "patients"
DB_USER = "ldhblrprodreadonly"

# Yahan jo password tumhe mila hai wo paste karo
DB_PASSWORD = "digitallyfeprod!1234"


# ==========================
# DATABASE CONNECTION
# ==========================
try:

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode="require",
        connect_timeout=10
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            CURRENT_DATABASE(),
            CURRENT_USER,
            NOW();
    """)

    db_name, db_user, db_time = cursor.fetchone()

    st.success("✅ Database Connected Successfully!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Status", "Connected")
    col2.metric("Database", db_name)
    col3.metric("User", db_user)

    st.write("Database Time:", db_time)

    cursor.close()
    conn.close()

except Exception as e:

    st.error("❌ Database Connection Failed")

    st.write("Error details:")

    st.code(str(e))