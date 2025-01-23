import streamlit as st

def load_allowed_users(file_path):
    config = toml.load(file_path)
    return config["users"]["allowed"]

def get_username_from_url():
    query_params = st.experimental_get_query_params()
    username = query_params.get("Username", [None])[0]
    return username

def main():
    st.title("Accesso Applicazione")

    allowed_users = load_allowed_users("users.toml")
    username = get_username_from_url()

    if username is None:
        st.warning("Non è stato fornito alcun parametro 'Username' nell'URL.")
    elif username in allowed_users:
        st.success(f"Benvenuto, {username}!")
        st.write("Ora puoi accedere all'app.")
    else:
        st.error("Accesso negato: non sei autorizzato a usare questa applicazione.")

if __name__ == "__main__":
    main()
