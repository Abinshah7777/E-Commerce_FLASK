class CatalogueNotFoundError(Exception):
    """Raised when a catalogue entry is not found in the database."""
    pass


class InvalidCatalogueInputError(Exception):
    """Raised when input data for a catalogue is invalid or malformed."""
    pass


class DatabaseConnectionError(Exception):
    """Raised when the database connection fails."""
    pass
