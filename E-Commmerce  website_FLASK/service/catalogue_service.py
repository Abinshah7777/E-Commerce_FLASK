from dto.catalogue_dto import Catalogue
from util.db_get_connection import get_connection

class CatalogueService:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def create_catalogue(self, catalogue: Catalogue):
        query = """
            INSERT INTO catalogue (catalogue_id, catalogue_name, catalogue_version, 
                                   is_cat_active, catalogue_start, catalogue_end)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (catalogue.catalogue_id,
            catalogue.catalogue_name,
            catalogue.catalogue_version,
            catalogue.is_cat_active,
            catalogue.catalogue_start,
            catalogue.catalogue_end)
        self.cursor.execute(query, data)
        self.conn.commit()

    def get_catalogue_by_id(self, catalogue_id):
        self.cursor.execute("SELECT * FROM catalogue WHERE catalogue_id = %s", (catalogue_id,))
        row = self.cursor.fetchone()
        return Catalogue(*row) if row else None

    def update_catalogue_by_id(self, catalogue_id, updated_catalogue: Catalogue):
        query = """
            UPDATE catalogue
            SET catalogue_name = %s, catalogue_version = %s,
                is_cat_active = %s, catalogue_start = %s, catalogue_end = %s
            WHERE catalogue_id = %s
        """
        data = (
            updated_catalogue.catalogue_name,
            updated_catalogue.catalogue_version,
            updated_catalogue.is_cat_active,
            updated_catalogue.catalogue_start,
            updated_catalogue.catalogue_end,
            catalogue_id
        )
        self.cursor.execute(query, data)
        self.conn.commit()

    def delete_catalogue_by_id(self, catalogue_id):
        self.cursor.execute("DELETE FROM catalogue WHERE catalogue_id = %s", (catalogue_id,))
        self.conn.commit()

    def get_all_catalogues(self):
        self.cursor.execute("SELECT * FROM catalogue")
        rows = self.cursor.fetchall()
        return [Catalogue(*row) for row in rows]
