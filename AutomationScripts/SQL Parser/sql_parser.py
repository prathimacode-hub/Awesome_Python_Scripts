from sql_metadata import Parser

rawsql = """
        select id, name, sum(amount) as total_amt from schema.foo a
        left join ( select id, name from schema.bar limit 10 ) b on a.id = b.id
        -- left join schema_b.bars c on b.id = c.id
        left join schema_b.foos c on b.id = c.id
        group by id, name
        limit 1000
        """

# initial Parser
sql_parser = Parser(rawsql)

# example sql_parser
sql_parser_columns = sql_parser.columns
print("## exact columns form sql")
print(sql_parser_columns)

sql_parser_tables = sql_parser.tables
print("## exact schema and table form sql")
print(sql_parser_tables)

sql_parser_columns_aliases = sql_parser.columns_aliases
print("## exact columns_aliases form sql")
print(sql_parser_columns_aliases)

sql_parser_subqueries = sql_parser.subqueries
print("## exact subqueries form sql")
print(sql_parser_subqueries)


