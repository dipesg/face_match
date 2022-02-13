mkdir -p  ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
headless = true\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml