class Catalogue:
    def __init__(self, catalogue_id, catalogue_name, catalogue_version,
                 is_cat_active, catalogue_start, catalogue_end):
        self.catalogue_id = catalogue_id
        self.catalogue_name = catalogue_name
        self.catalogue_version = catalogue_version
        self.is_cat_active = is_cat_active
        self.catalogue_start = catalogue_start
        self.catalogue_end = catalogue_end

    def __str__(self):
        return (f"Catalogue ID: {self.catalogue_id}, "
                f"Name: {self.catalogue_name}, "
                f"Version: {self.catalogue_version}, "
                f"Active: {'Yes' if self.is_cat_active else 'No'}, "
                f"Start: {self.catalogue_start}, "
                f"End: {self.catalogue_end}")
