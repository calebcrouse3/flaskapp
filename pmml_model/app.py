@app.route('/health', methods=['POST'])
def app_status():
    return f"{status.HTTP_200_OK}"


@app.route('/load', methods=['POST'])
def load_model():
    file_path = request.data.decode("utf-8")
    is_load_ok = load_callback(file_path)
    return f"{status.HTTP_200_OK}" if is_load_ok else f"{status.HTTP_500_INTERNAL_SERVER_ERROR}"


@app.route('/unload', methods=['POST'])
def unload_model():
    file_path = request.data.decode("utf-8")
    is_unload_ok = unload_callback(file_path)
    return f"{status.HTTP_200_OK}" if is_unload_ok else f"{status.HTTP_500_INTERNAL_SERVER_ERROR}"


@app.route("/predict", methods=['POST'])
def predict():
    json_data = request.get_json()
    prediction = predict_callback(json_data)
    return f'{prediction}'

...
@app.route("/info", methods=['GET'])
def get_models_info():
    models_info = {}
    for model_name, model in models.items():
        print(model.targetFields)
        models_info.update({
            model_name: {
                'features': model.inputNames,
                'outputs': model.outputNames
            }
        })
    return models_info


if __name__ == "__main__":
    app.run(debug=cfg['app']['debug'], port=cfg['app']['port'])