from models.database import Database
from typing import Optional, Self, Any
from sqlite3 import Cursor


class MustWatch:
 
    def __init__(
        self: Self,
        titulo_item: Optional[str],
        tipo_item: Optional[str],
        indicado_por: Optional[str],
        id_item: Optional[int] = None
    ) -> None:

        self.titulo_item = titulo_item
        self.tipo_item = tipo_item
        self.indicado_por = indicado_por
        self.id = id_item

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = """
            SELECT titulo_item, tipo_item, indicado_por, id_item
            FROM mustwatch
            WHERE id_item = ?;
            """
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)

            [[titulo, tipo, indicado, id_item]] = resultado

        return cls(titulo, tipo, indicado, id_item)

    def salvar_item(self) -> None:
        with Database() as db:
            query: str = """
            INSERT INTO mustwatch
            (titulo_item, tipo_item, indicado_por)
            VALUES (?, ?, ?);
            """
            params: tuple = (
                self.titulo_item,
                self.tipo_item,
                self.indicado_por
            )
            db.executar(query, params)

    @classmethod
    def obter_lista(cls) -> list[Self]:
        with Database() as db:
            query: str = """
            SELECT titulo_item, tipo_item, indicado_por, id_item
            FROM mustwatch;
            """
            resultados: list[Any] = db.buscar_tudo(query)

            return [
                cls(titulo, tipo, indicado, id_item)
                for titulo, tipo, indicado, id_item in resultados
            ]

    def excluir_item(self) -> Cursor:
        with Database() as db:
            query: str = "DELETE FROM mustwatch WHERE id_item = ?;"
            params: tuple = (self.id,)
            return db.executar(query, params)

    def atualizar_item(self) -> Cursor:
        with Database() as db:
            query: str = """
            UPDATE mustwatch
            SET titulo_item = ?, tipo_item = ?, indicado_por = ?
            WHERE id_item = ?;
            """
            params: tuple = (
                self.titulo_item,
                self.tipo_item,
                self.indicado_por,
                self.id
            )
            return db.executar(query, params)
