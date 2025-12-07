# Composition 设计模式：生产级实践指南

## 核心概念

**Composition（组合）** 是一种设计原则，通过 **"Has-A"** 关系而非 **"Is-A"** 继承关系来构建复杂对象。它遵循 SOLID 原则中的 **"组合优于继承"** (Composition over Inheritance)。

---

## 生产级代码示例

### 场景：电商订单系统

以下是一个真实的电商订单系统实现，展示如何使用 Composition 构建可维护、可测试的代码。

```python
"""
电商订单系统 - Composition 设计模式实践

本模块演示如何使用组合模式构建灵活的订单系统，包括：
- 用户信息管理
- 商品清单管理
- 支付处理
- 物流追踪
"""

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from uuid import uuid4

class OrderStatus(Enum):
    """订单状态枚举"""
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentMethod(Enum):
    """支付方式枚举"""
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    ALIPAY = "alipay"
    WECHAT_PAY = "wechat_pay"

@dataclass
class Address:
    """
    地址信息值对象 (Value Object)
    
    Attributes:
        street: 街道地址
        city: 城市
        state: 省/州
        postal_code: 邮政编码
        country: 国家代码 (ISO 3166-1 alpha-2)
    """
    street: str
    city: str
    state: str
    postal_code: str
    country: str = "CN"
    
    def __post_init__(self):
        """验证地址字段的有效性"""
        if not all([self.street, self.city, self.state, self.postal_code]):
            raise ValueError("所有地址字段都必须填写")
    
    def format_full_address(self) -> str:
        """
        格式化完整地址用于显示
        
        Returns:
            格式化的地址字符串
        """
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"

@dataclass
class Customer:
    """
    客户信息聚合根 (Aggregate Root)
    
    Composition: Customer HAS-A Address (而不是 Customer IS-A Address)
    
    Attributes:
        customer_id: 客户唯一标识
        name: 客户姓名
        email: 电子邮件
        phone: 联系电话
        billing_address: 账单地址
        shipping_address: 配送地址（可选，默认使用账单地址）
    """
    customer_id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    email: str = ""
    phone: str = ""
    billing_address: Optional[Address] = None
    shipping_address: Optional[Address] = None
    
    def get_shipping_address(self) -> Address:
        """
        获取配送地址，如果未设置则使用账单地址
        
        Returns:
            有效的配送地址对象
            
        Raises:
            ValueError: 当两个地址都未设置时
        """
        if self.shipping_address:
            return self.shipping_address
        if self.billing_address:
            return self.billing_address
        raise ValueError("客户必须至少设置一个地址")

@dataclass
class Product:
    """
    商品实体 (Entity)
    
    Attributes:
        product_id: 商品唯一标识 (SKU)
        name: 商品名称
        price: 单价（使用 Decimal 避免浮点误差）
        weight_kg: 重量（千克）
        description: 商品描述
    """
    product_id: str
    name: str
    price: Decimal
    weight_kg: Decimal = Decimal("0.0")
    description: str = ""
    
    def __post_init__(self):
        """验证商品数据的有效性"""
        if self.price < 0:
            raise ValueError("商品价格不能为负数")
        if self.weight_kg < 0:
            raise ValueError("商品重量不能为负数")

@dataclass
class OrderItem:
    """
    订单项值对象 (Value Object)
    
    Composition: OrderItem HAS-A Product
    代表订单中的单个商品及其数量
    
    Attributes:
        product: 商品对象引用
        quantity: 购买数量
    """
    product: Product
    quantity: int = 1
    
    def __post_init__(self):
        """验证订单项的有效性"""
        if self.quantity <= 0:
            raise ValueError("商品数量必须大于 0")
    
    def calculate_subtotal(self) -> Decimal:
        """
        计算该订单项的小计金额
        
        Returns:
            小计金额（商品单价 × 数量）
        """
        return self.product.price * self.quantity
    
    def calculate_weight(self) -> Decimal:
        """
        计算该订单项的总重量
        
        Returns:
            总重量（单品重量 × 数量）
        """
        return self.product.weight_kg * self.quantity

@dataclass
class Payment:
    """
    支付信息值对象 (Value Object)
    
    Attributes:
        payment_method: 支付方式
        transaction_id: 第三方交易流水号
        amount: 支付金额
        paid_at: 支付时间
    """
    payment_method: PaymentMethod
    transaction_id: str
    amount: Decimal
    paid_at: datetime = field(default_factory=datetime.now)
    
    def is_valid(self) -> bool:
        """
        验证支付信息的有效性
        
        Returns:
            支付信息是否有效
        """
        return (
            bool(self.transaction_id) and
            self.amount > 0 and
            self.paid_at <= datetime.now()
        )

@dataclass
class Shipping:
    """
    物流信息值对象 (Value Object)
    
    Attributes:
        tracking_number: 物流追踪号
        carrier: 物流承运商
        shipped_at: 发货时间
        estimated_delivery: 预计送达时间
    """
    tracking_number: str = ""
    carrier: str = ""
    shipped_at: Optional[datetime] = None
    estimated_delivery: Optional[datetime] = None
    
    def is_shipped(self) -> bool:
        """判断订单是否已发货"""
        return bool(self.tracking_number and self.shipped_at)

@dataclass
class Order:
    """
    订单聚合根 (Aggregate Root)
    
    这是 Composition 的核心示例：
    - Order HAS-A Customer（客户信息）
    - Order HAS-A List[OrderItem]（订单项列表）
    - Order HAS-A Payment（支付信息）
    - Order HAS-A Shipping（物流信息）
    
    每个组件都是独立的、可复用的、职责单一的对象
    
    Attributes:
        order_id: 订单唯一标识
        customer: 客户对象引用
        items: 订单项列表
        payment: 支付信息（可选）
        shipping: 物流信息
        status: 订单状态
        created_at: 创建时间
    """
    order_id: str = field(default_factory=lambda: str(uuid4()))
    customer: Optional[Customer] = None
    items: List[OrderItem] = field(default_factory=list)
    payment: Optional[Payment] = None
    shipping: Shipping = field(default_factory=Shipping)
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """
        添加商品到订单
        
        Args:
            product: 要添加的商品对象
            quantity: 购买数量
            
        Raises:
            ValueError: 当商品数量无效时
        """
        if quantity <= 0:
            raise ValueError("商品数量必须大于 0")
        
        # 检查商品是否已存在，如果存在则累加数量
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        
        # 添加新商品
        self.items.append(OrderItem(product=product, quantity=quantity))
    
    def calculate_total(self) -> Decimal:
        """
        计算订单总金额
        
        Returns:
            订单总金额（所有订单项小计之和）
        """
        return sum(
            item.calculate_subtotal() for item in self.items
        )
    
    def calculate_total_weight(self) -> Decimal:
        """
        计算订单总重量（用于物流计费）
        
        Returns:
            订单总重量（千克）
        """
        return sum(
            item.calculate_weight() for item in self.items
        )
    
    def process_payment(
        self,
        payment_method: PaymentMethod,
        transaction_id: str
    ) -> None:
        """
        处理订单支付
        
        Args:
            payment_method: 支付方式
            transaction_id: 第三方交易流水号
            
        Raises:
            ValueError: 当订单状态不允许支付或金额不匹配时
        """
        if self.status != OrderStatus.PENDING:
            raise ValueError(f"订单状态为 {self.status.value}，无法支付")
        
        total_amount = self.calculate_total()
        self.payment = Payment(
            payment_method=payment_method,
            transaction_id=transaction_id,
            amount=total_amount
        )
        
        if not self.payment.is_valid():
            raise ValueError("支付信息无效")
        
        self.status = OrderStatus.PAID
    
    def ship_order(
        self,
        tracking_number: str,
        carrier: str,
        estimated_delivery: datetime
    ) -> None:
        """
        发货订单
        
        Args:
            tracking_number: 物流追踪号
            carrier: 物流承运商
            estimated_delivery: 预计送达时间
            
        Raises:
            ValueError: 当订单未支付或已发货时
        """
        if self.status != OrderStatus.PAID:
            raise ValueError(f"订单状态为 {self.status.value}，无法发货")
        
        self.shipping = Shipping(
            tracking_number=tracking_number,
            carrier=carrier,
            shipped_at=datetime.now(),
            estimated_delivery=estimated_delivery
        )
        self.status = OrderStatus.SHIPPED
    
    def get_order_summary(self) -> dict:
        """
        生成订单摘要信息（用于 API 响应或报表）
        
        Returns:
            包含订单关键信息的字典
        """
        return {
            "order_id": self.order_id,
            "customer_name": self.customer.name if self.customer else "Unknown",
            "item_count": len(self.items),
            "total_amount": float(self.calculate_total()),
            "total_weight_kg": float(self.calculate_total_weight()),
            "status": self.status.value,
            "is_paid": self.payment is not None and self.payment.is_valid(),
            "is_shipped": self.shipping.is_shipped(),
            "created_at": self.created_at.isoformat()
        }

# ==================== 使用示例 ====================

def main():
    """
    完整的订单处理流程示例
    演示如何使用 Composition 构建的订单系统
    """
    # 1. 创建客户信息
    customer = Customer(
        name="张三",
        email="zhangsan@example.com",
        phone="13800138000",
        billing_address=Address(
            street="中关村大街1号",
            city="北京",
            state="北京市",
            postal_code="100080"
        )
    )
    
    # 2. 创建商品
    laptop = Product(
        product_id="SKU-001",
        name="ThinkPad X1 Carbon",
        price=Decimal("8999.00"),
        weight_kg=Decimal("1.13"),
        description="14英寸商务笔记本"
    )
    
    mouse = Product(
        product_id="SKU-002",
        name="罗技 MX Master 3",
        price=Decimal("699.00"),
        weight_kg=Decimal("0.14"),
        description="无线蓝牙鼠标"
    )
    
    # 3. 创建订单并添加商品
    order = Order(customer=customer)
    order.add_item(laptop, quantity=1)
    order.add_item(mouse, quantity=2)
    
    print("=" * 50)
    print("订单创建成功")
    print(f"订单号: {order.order_id}")
    print(f"商品总数: {len(order.items)}")
    print(f"订单金额: ¥{order.calculate_total()}")
    print(f"总重量: {order.calculate_total_weight()} kg")
    
    # 4. 处理支付
    order.process_payment(
        payment_method=PaymentMethod.ALIPAY,
        transaction_id="TXN-20250619-001"
    )
    print(f"\n支付成功 - 状态: {order.status.value}")
    
    # 5. 发货
    order.ship_order(
        tracking_number="SF1234567890",
        carrier="顺丰速运",
        estimated_delivery=datetime(2025, 6, 21, 18, 0)
    )
    print(f"已发货 - 追踪号: {order.shipping.tracking_number}")
    
    # 6. 获取订单摘要
    print("\n" + "=" * 50)
    print("订单摘要")
    print("=" * 50)
    summary = order.get_order_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```

---

## Composition 的生产级优势

### 1. 可测试性 (Testability)

```python
def test_order_total_calculation():
    """测试订单金额计算 - 无需依赖真实数据库"""
    product = Product("TEST-001", "测试商品", Decimal("100.00"))
    order = Order()
    order.add_item(product, quantity=2)
    
    assert order.calculate_total() == Decimal("200.00")
```

### 2. 可维护性 (Maintainability)

- **单一职责**：每个类只负责一件事（`Address` 管地址，`Payment` 管支付）
- **易于修改**：修改 `Shipping` 逻辑不影响 `Order` 的其他部分
- **降低耦合**：组件之间通过接口交互，不直接依赖实现

### 3. 可复用性 (Reusability)

```python
# Address 类可以在多个场景复用
class Warehouse:
    """仓库实体也需要地址信息"""
    def __init__(self, name: str, location: Address):
        self.name = name
        self.location = location  # 复用 Address 类
```

### 4. 可扩展性 (Extensibility)

```python
# 新增优惠券功能，无需修改现有代码
@dataclass
class Coupon:
    """优惠券值对象"""
    code: str
    discount_percent: Decimal
    
    def apply_discount(self, amount: Decimal) -> Decimal:
        """应用折扣"""
        return amount * (1 - self.discount_percent / 100)

# 在 Order 类中添加组合
@dataclass
class Order:
    # ... 现有字段 ...
    coupon: Optional[Coupon] = None  # 新增：Order HAS-A Coupon
    
    def calculate_total(self) -> Decimal:
        """计算订单总金额（含折扣）"""
        subtotal = sum(item.calculate_subtotal() for item in self.items)
        if self.coupon:
            return self.coupon.apply_discount(subtotal)
        return subtotal
```

---

>[!tip]
>**Composition vs Inheritance 选择指南**
>- **选 Composition**：
>  - 需要运行时动态组合行为（如订单可选地添加优惠券）
>  - 需要多个独立功能的组合（Order 需要 Payment + Shipping + Customer）
>  - 需要避免深层继承链导致的脆弱性
>- **选 Inheritance**：
>  - 存在明确的 "Is-A" 关系（如 `ElectricCar` IS-A `Car`）
>  - 需要利用多态性（如不同类型的 `Shape` 有不同的 `draw()` 实现）
>  - 子类需要重写父类的核心行为

>[!note]
>**生产环境最佳实践**
>1. **使用类型注解**：提高代码可读性和 IDE 支持
>2. **数据类 (dataclass)**：减少样板代码，自动生成 `__init__`、`__repr__` 等方法
>3. **值对象不可变**：使用 `frozen=True` 确保 `Address`、`Payment` 等值对象创建后不可修改
>4. **聚合根控制边界**：只通过 `Order` 操作其内部组件，不直接修改 `OrderItem`
>5. **使用 Decimal 处理金额**：避免浮点数精度问题
>6. **异常处理**：在边界条件抛出明确的异常，而不是返回 `None`