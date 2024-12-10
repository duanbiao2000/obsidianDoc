

下面是一个简单的例子，展示了如何使用JDBC API连接到MySQL数据库并执行一个查询：

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JdbcExample {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        try {
            // 加载驱动程序（在Java 6及以上版本中通常是不必要的）
            // Class.forName("com.mysql.cj.jdbc.Driver");

            // 获取数据库连接
            String url = "jdbc:mysql://localhost:3306/mydatabase";
            String user = "root";
            String password = "password";
            conn = DriverManager.getConnection(url, user, password);

            // 创建SQL语句对象
            String sql = "SELECT id, name FROM users WHERE active = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setBoolean(1, true);

            // 执行查询
            rs = pstmt.executeQuery();

            // 处理结果集
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                System.out.println("ID: " + id + ", Name: " + name);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // 关闭资源
            try { if (rs != null) rs.close(); } catch (SQLException e) { /* ignored */ }
            try { if (pstmt != null) pstmt.close(); } catch (SQLException e) { /* ignored */ }
            try { if (conn != null) conn.close(); } catch (SQLException e) { /* ignored */ }
        }
    }
}
```

这段代码演示了典型的JDBC流程，包括连接到数据库、准备并执行SQL语句、处理结果以及最后关闭所有打开的资源。