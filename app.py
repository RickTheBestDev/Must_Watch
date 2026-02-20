from flask import Flask, render_template, request, redirect, url_for
from models.item import MustWatch
from models.database import init_db

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("home.html", titulo="Must Watch")


@app.route("/lista", methods=["GET", "POST"])
def lista():

    if request.method == "POST":
        titulo = request.form["titulo-item"]
        tipo = request.form["tipo-item"]
        indicado = request.form["indicado-por"]

        item = MustWatch(titulo, tipo, indicado)
        item.salvar_item()

        return redirect(url_for("lista"))

    itens = MustWatch.obter_lista()

    return render_template(
        "lista.html",
        titulo="Lista Must Watch",
        itens=itens
    )


@app.route("/delete/<int:idItem>")
def delete(idItem):
    item = MustWatch.id(idItem)
    item.excluir_item()
    return redirect(url_for("lista"))


@app.route("/update/<int:idItem>", methods=["GET", "POST"])
def update(idItem):

    if request.method == "POST":
        titulo = request.form["titulo-item"]
        tipo = request.form["tipo-item"]
        indicado = request.form["indicado-por"]

        item = MustWatch(titulo, tipo, indicado, idItem)
        item.atualizar_item()
        return redirect(url_for("lista"))

    itens = MustWatch.obter_lista()
    item_selecionado = MustWatch.id(idItem)

    return render_template(
        "lista.html",
        titulo="Editando item",
        itens=itens,
        item_selecionado=item_selecionado
    )


@app.route("/ola")
def ola():
    return "Olá, Mundo!"
