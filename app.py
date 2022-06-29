from flask import Flask, render_template, request, redirect, Response, flash
from xml_to_json_convertor import convertEmployeesInfoXmlToOrdersJson, isaAllowedFile, placeOrder

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def uploadXmlFile():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and isaAllowedFile(file.filename):
            order_json = convertEmployeesInfoXmlToOrdersJson(file.read())
            response = placeOrder(order_json)
            return render_template("response.html",
                                   response_json=response["response_json"],
                                   response_text=response["response_text"])
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
