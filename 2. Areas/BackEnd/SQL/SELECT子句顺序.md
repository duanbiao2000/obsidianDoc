# SELECT子句顺序



| 子句     | 说明               | 是否必须使用           |
| -------- | ------------------ | ---------------------- |
| SELECT   | 要返回的列或表达式 | 是                     |
| FROM     | 从中检索数据的表   | 仅在从表选择数据时使用 |
| WHERE    | 行级过滤           | 否                     |
| GROUP BY | 分组说明           | 仅在按组计算聚集时使用 |
| HAVING   | 组级过滤           | 否                     |
| ORDER BY | 输出排序顺序       | 否                     |

inner-jion

``` sql
SELECT 
    prod_name, vend_name, prod_price, quantity
FROM
    orderitems,
    products,
    vendors
WHERE
    products.vend_id = vendors.vend_id
        AND orderitems.prod_id = products.prod_id
        AND order_num = 20007;
        
```

| prod_name           | vend_name       | prod_price | quantity |
| ------------------- | --------------- | ---------- | -------- |
| 18 inch teddy bear  | Bears R Us      | 11.99      | 50       |
| Fish bean bag toy   | Doll House Inc. | 3.49       | 100      |
| Bird bean bag toy   | Doll House Inc. | 3.49       | 100      |
| Rabbit bean bag toy | Doll House Inc. | 3.49       | 100      |
| Raggedy Ann         | Doll House Inc. | 4.99       | 50       |

self-join

# 用自连接不用而不用子查询
. DBMS处理联结远比处理子查询快得多.

```sql
SELECT 
    cust_id, cust_name, cust_contact
FROM
    customers
WHERE
    cust_name = (SELECT 
            cust_name
        FROM
            customers
        WHERE
            cust_contact = 'Jim Jones')
```

| cust_id    | cust_name | cust_contact       |
| ---------- | --------- | ------------------ |
| 1000000003 | Fun4All   | Jim Jones          |
| 1000000004 | Fun4All   | Denise L. Stephens |

```mysql
SELECT 
    c1.cust_id, c1.cust_name, c1.cust_contact
FROM
    customers AS c1,
    customers AS c2
WHERE
    c1.cust_name = c2.cust_name
        AND c2.cust_contact = 'Jim Jones';
```

| cust_id    | cust_name | cust_contact       |
| ---------- | --------- | ------------------ |
| 1000000003 | Fun4All   | Jim Jones          |
| 1000000004 | Fun4All   | Denise L. Stephens |

nature join



outer join

