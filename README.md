
# Environment Set up
Create virtual environment with conda
```
conda create -n udacity python=3.8
conda activate udacity
```
Install dependencies:
```
pip install -r requirements.txt
```

## Training

For training Random Forest
```
python starter/train_model.py
```
Or can run the api for inference (port 5000)

```
python main.py
```
# API
To send request to API

```
python render_fastapi_request.py
```

# Testing

```
pytest test -vv
```
