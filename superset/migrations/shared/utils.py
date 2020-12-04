from alembic import op
from sqlalchemy import engine_from_config
from sqlalchemy.engine import reflection


def table_has_column(table: str, column: str) -> bool:
    """
    Checks if a column exists in a given table.

    :param table: A table name
    :param column: A column name
    :returns: True iff the column exists in the table
    """

    config = op.get_context().config
    engine = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy."
    )
    insp = reflection.Inspector.from_engine(engine)
    has_column = False
    for col in insp.get_columns(table):
        if column != col["name"]:
            continue
        has_column = True
    return has_column
