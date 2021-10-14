## SQL Parser

## Short description of package/script: 
Extracts column names and tables used by the query. Automatically conduct column alias resolution, sub queries aliases resolution as well as tables aliases resolving.

Provides also a helper for normalization of SQL queries.

## List out the libraries imported: 
```` 
pip install sql-metadata
```` 

## Example extracting raw sql
## Input

```sql
select id, name, sum(amount) as total_amt from schema.foo a
left join ( select id, name from schema.bar limit 10 ) b on a.id = b.id
-- left join schema_b.bars c on b.id = c.id
left join schema_b.foos c on b.id = c.id
group by id, name
limit 1000
```

## Output

### sql_parser.columns
````
['id', 'name', 'amount', 'schema.foo.id', 'schema_b.foos.id']
````

### sql_parser.tables
````
['schema.foo', 'schema.bar', 'schema_b.foos']
````

### sql_parser.columns_aliases
````
{'total_amt': 'amount'}
````

### sql_parser.subqueries
````
{'b': 'select id, name from schema.bar limit 10'}
````
