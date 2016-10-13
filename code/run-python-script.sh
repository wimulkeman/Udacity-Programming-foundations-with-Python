if [[ "$#" -lt 1 ]]; then
    echo "Geef een filenaam op"
fi

docker run -it --rm --name python-udacity -v "$PWD":/code -w /code python:2 python $1
