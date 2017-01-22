if [[ "$#" -lt 1 ]]; then
    echo "Geef een filenaam op"
fi

docker run -it --rm -v "$PWD":/code -w /code udacity-python python $1
