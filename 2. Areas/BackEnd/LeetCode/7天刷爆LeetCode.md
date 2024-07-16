---
aliases: null
theme: null
original: null
url: null
author: null
created_date: 2023-07-16 21:25
date updated: 2024-07-16 21:25
type: null
high priority: false
---

# 83.删除排序链表中的重复元素

给定一个已排序的链表的头 `head` ， _删除所有重复的元素，使每个元素只出现一次_ 。返回 _已排序的链表_ 。

![img](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)

```
输入：head = [1,1,2]
输出：[1,2]
```

![img](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)

```
输入：head = [1,1,2,3,3]
输出：[1,2,3]
```

**提示：**

- 链表中节点数目在范围 `[0, 300]` 内
- `-100 <= Node.val <= 100`
- 题目数据保证链表已经按升序 **排列**

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
//方式1:遍历方式
class Solution {   
    public ListNode deleteDuplicates(ListNode head) {
       if (head == null) {  //边界条件
           return head;
       }
       ListNode currentNode = head; 
       while(null != currentNode.next){  //遍历原始列表(ListNode head)
           if(currentNode.next.val == currentNode.val){ //判断当前节点值是否与下一个结点值相等
               currentNode.next = currentNode.next.next; //如果相等越过下一个结点,转而将当前结点指向下一个结点的后续结点 currentNode.next.next
           }else {
               currentNode = currentNode.next; //如果不相等,则当前结点保留
           }
       }
       return head ;
    }
}
```

# 141.环形链表

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：pos 不作为参数进行传递 **。仅仅是为了标识链表的实际情况。

_如果链表中存在环_ ，则返回 `true` 。 否则，返回 `false` 。

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 //环形列表通用思想:Floyd解法 , 快慢双指针.(奥数:环形追击问题)
public class Solution {  
    public boolean hasCycle(ListNode head) {
        if (head ==null) return false;  //防御编码
        ListNode slowPtr = head, fastPtr = head;
        while (fastPtr.next != null && fastPtr.next.next!=null){  //快指针指向null值,则一定没有环
            slowPtr = slowPtr.next; //慢指针每次一跳
            fastPtr = fastPtr.next.next; //快指针每次两跳,追击得到则为环链
            if (slowPtr == fastPtr)
            return true;
        }
        return false;
    }
}
```

# [160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

难度简单2039

给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交**：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

四种方法: 穷举 / hash map /  双指针 / 计算双链长度差,然后将较长链表一次移动长度差的节点以后,再同时移动两个指针,如相交则必在某节点相遇.

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    //方案1:双指针,当移动到null,则将该指针跳转到另一链表头部
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // if(headA == null || headB == null){
        //     return null;
        // }
        // ListNode pA = headA, pB = headB;
        // while(pA != pB){
        //     pA = pA == null ? headB : pA.next;
        //     pB = pB == null ? headA : pB.next;
        // }
        // return pA;

    //方案2: 两列表长度差d= m-n  O(m+n) O(1)
        int L1=0,L2=0,diff=0;
        ListNode head1 = headA , head2=headB;
        while(head1 != null){
            L1++;
            head1= head1.next;
        }
        while(head2 != null){
            L2++;
            head2= head2.next;
        }
        if(L1<L2){
            head1 = headB; head2 = headA; diff = L2-L1;
        }else{
            head1 = headA; head2 = headB; diff = L1-L2;
        }
        for(int i=0;i<diff;i++)
            head1 = head1.next;
        while(head1!=null && head2 !=null){
            if(head1==head2)
                return head1;
            head1=head1.next;
            head2=head2.next;
        }
        return null;
    }
}
```

# [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)

```
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
```

![img](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**示例 1：**

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

![1680231286821](1680231286821.png)

![1680231456055](1680231456055.png)

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode preNode = null; //临时节点用于单链表交换翻转
        ListNode curr = head;
        while(curr!=null){
            ListNode next = curr.next;
            curr.next = preNode;
            preNode = curr;
            curr = next;
        }
        return preNode;
    }
}
```

# [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
输入：head = [1,2,2,1]
输出：true
```

**提示：**

- 链表中节点数目在范围`[1, 105]` 内
- `0 <= Node.val <= 9`

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head, slow = head;
        while (fast!=null && fast.next!=null){
            fast = fast.next.next;
            slow = slow.next;
        }
        //如果链表是奇数节点,把正中的归到左边
        if(fast!=null){ //此时快指针在奇数链表末尾
            slow= slow.next; //慢指针再前进一位
        }
        slow = reverse(slow);
        fast = head;  //反转完成后,将快指针重新移动到头部
        
        while(slow!=null){ //一一开始值的相关比较
            if(fast.val!=slow.val){
                return false;
            }
            fast = fast.next;
            slow = slow.next;
        }
        return true;
    }
    //反转链表
    public ListNode reverse(ListNode head){
        ListNode prev = null;
        while (head!=null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}
```
