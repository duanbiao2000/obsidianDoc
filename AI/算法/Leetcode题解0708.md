三道 LeetCode 简单难度的题目，并提供使用 JavaScript 的代码解答和测试用例，每个代码块都包含详细的注释：已经解答过的题目尽量不用再出现
1. 两数之和（Two Sum）
```javascript
const twoSum = function(nums, target) {
  // 创建一个空对象，用于保存数字和它们的索引
  const numMap = {};
  // 遍历数组
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;
    // 如果补数存在于 numMap 中，说明找到了答案
    if (complement in numMap) {
      return [numMap[complement], i];
    }
    // 否则，将当前数字及其索引保存到 numMap 中
    numMap[num] = i;
  }
};
```
2. 整数反转（Reverse Integer）
```javascript
const reverse = function(x) {
  let reversed = 0;
  // 循环将 x 的最后一位数字依次加到 reversed 中
  while (x !== 0) {
    const digit = x % 10;
    reversed = reversed * 10 + digit;
    // 检查是否溢出
    if (reversed < Math.pow(-2, 31) || reversed > Math.pow(2, 31) - 1) {
      return 0;
    }
    // 更新 x
    x = Math.trunc(x / 10);
  }
  return reversed;
};
```
3. 回文数（Palindrome Number）
```javascript
const isPalindrome = function(x) {
  // 如果 x 是负数或者末尾是 0 且 x 不为 0，则不是回文数
  if (x < 0 || (x % 10 === 0 && x !== 0)) {
    return false;
  }
  let reversed = 0;
  let original = x;
  // 反转后半部分数字
  while (original > reversed) {
    const digit = original % 10;
    reversed = reversed * 10 + digit;
    original = Math.trunc(original / 10);
  }
  // 如果原始数字长度是奇数，则反转后的数字需要去掉中间的数字
  return original === reversed || original === Math.trunc(reversed / 10);
};
```
4. 罗马数字转整数（Roman to Integer）
```javascript
const romanToInt = function(s) {
  // 创建一个罗马数字和对应整数的映射
  const romanToIntMap = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  };
  let result = 0;
  // 遍历输入的罗马数字字符串
  for (let i = 0; i < s.length; i++) {
    const currentInt = romanToIntMap[s[i]];
    const nextInt = romanToIntMap[s[i + 1]];
    // 如果当前的整数值比下一个整数值小，则减去当前整数值
    if (nextInt && currentInt < nextInt) {
      result -= currentInt;
    } else {
      result += currentInt;
    }
  }
  return result;
};
```
5. 最长公共前缀（Longest Common Prefix）
```javascript
const longestCommonPrefix = function(strs) {
  // 如果输入数组为空，则返回空字符串
  if (strs.length === 0) {
    return '';
  }
  // 将第一个字符串作为初始的公共前缀
  let prefix = strs[0];
  // 遍历剩余的字符串
  for (let i = 1; i < strs.length; i++) {
    // 如果当前字符串不是以 prefix 开头，则不断缩短 prefix
    while (strs[i].indexOf(prefix) !== 0) {
      prefix = prefix.substring(0, prefix.length - 1);
      // 如果 prefix 变为空字符串，则直接返回
      if (prefix === '') {
        return '';
      }
    }
  }
  return prefix;
};
```
6. 有效的括号（Valid Parentheses）
```javascript
const isValid = function(s) {
  const stack = [];
  // 遍历字符串中的每个字符
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    // 如果是左括号，将其推入栈中
    if (char === '(' || char === '[' || char === '{') {
      stack.push(char);
    }
    // 如果是右括号
    else {
      // 如果栈为空或者栈顶的左括号与当前右括号不匹配，则返回 false
      if (
        stack.length === 0 ||
        (char === ')' && stack[stack.length - 1] !== '(') ||
        (char === ']' && stack[stack.length - 1] !== '[') ||
        (char === '}' && stack[stack.length - 1] !== '{')
      ) {
        return false;
      }
      // 如果匹配成功，将栈顶的左括号弹出
      stack.pop();
    }
  }
  // 如果栈为空，则说明所有括号都匹配成功
  return stack.length === 0;
};
```
7. 合并两个有序链表（Merge Two Sorted Lists）
```javascript
class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}
const mergeTwoLists = function(l1, l2) {
  // 创建一个头节点和一个指针节点
  const dummy = new ListNode(0);
  let current = dummy;
  // 遍历两个链表
  while (l1 !== null && l2 !== null) {
    // 将较小的值连接到当前节点后面
    if (l1.val < l2.val) {
      current.next = l1;
      l1 = l1.next;
    } else {
      current.next = l2;
      l2 = l2.next;
    }
    // 更新当前节点
    current = current.next;
  }
  // 如果有一个链表遍历完了，将另一个链表剩下的部分直接连接到当前节点后面
  if (l1 !== null) {
    current.next = l1;
        } else {
    current.next = l2;
  }

  // 返回合并后的链表
  return dummy.next;
};

```

8. 删除排序数组中的重复项（Remove Duplicates from Sorted Array）
```javascript
const removeDuplicates = function(nums) {
  // 如果数组长度为 0 或 1，则不需要删除重复项，直接返回原数组
  if (nums.length === 0 || nums.length === 1) {
    return nums.length;
  }
  let index = 0;
  // 遍历数组
  for (let i = 1; i < nums.length; i++) {
    // 如果当前元素与前一个元素不相等，则将当前元素放到 index+1 的位置
    if (nums[i] !== nums[index]) {
      index++;
      nums[index] = nums[i];
    }
  }
  // 返回去重后的数组长度
  return index + 1;
};
```
9. 实现 strStr()（Implement strStr()）
```javascript
const strStr = function(haystack, needle) {
  // 如果 needle 是空字符串，则返回 0
  if (needle === '') {
    return 0;
  }
  // 遍历 haystack
  for (let i = 0; i < haystack.length; i++) {
    // 如果 haystack 剩余的长度小于 needle，则不可能找到 needle，返回 -1
    if (haystack.length - i < needle.length) {
      return -1;
    }
    let j = 0;
    // 在 haystack 中从 i 开始逐个比较字符
    while (j < needle.length && haystack[i + j] === needle[j]) {
      j++;
    }
    // 如果 j 等于 needle 的长度，说明找到了 needle
    if (j === needle.length) {
      return i;
    }
  }
  // 如果遍历完 haystack 都没有找到 needle，则返回 -1
  return -1;
};
```
10. 外观数列（Count and Say）
```javascript
const countAndSay = function(n) {
  let result = '1';
  // 迭代 n-1 次
  for (let i = 1; i < n; i++) {
    let current = '';
    let count = 1;
    // 遍历上一个结果字符串
    for (let j = 0; j < result.length; j++) {
      // 如果当前字符与下一个字符相同，则计数加一
      if (result[j] === result[j + 1]) {
        count++;
      }
      // 如果不相同，则将计数和当前字符添加到 current 中，并重置计数为 1
      else {
        current += count + result[j];
        count = 1;
      }
    }
    // 更新结果字符串
    result = current;
  }
  return result;
};
```
这是十道 LeetCode 简单难度的题目的 JavaScript 代码解答。希望对你有帮助！

当然，我会给你提供三道不同的 LeetCode 简单难度的题目，并附上使用 JavaScript 的代码解答和测试用例。以下是题目和解答：
1. 移动零（Move Zeroes）
题目描述：
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例：
```javascript
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```
解答：
```javascript
const moveZeroes = function(nums) {
  let index = 0;
  // 遍历数组，将非零元素移动到数组的前面
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      nums[index] = nums[i];
      index++;
    }
  }
  // 将剩余的位置填充为 0
  for (let i = index; i < nums.length; i++) {
    nums[i] = 0;
  }
  return nums;
};
```
测试用例：
```javascript
console.log(moveZeroes([0, 1, 0, 3, 12])); // [1, 3, 12, 0, 0]
console.log(moveZeroes([0, 0, 0, 0, 0])); // [0, 0, 0, 0, 0]
console.log(moveZeroes([1, 2, 3, 4, 5])); // [1, 2, 3, 4, 5]
```
2. 反转字符串（Reverse String）
题目描述：
编写一个函数，其作用是将输入的字符串反转过来。
示例：
```javascript
输入: "hello"
输出: "olleh"
```
解答：
```javascript
const reverseString = function(s) {
  let left = 0;
  let right = s.length - 1;
  // 使用双指针，交换左右指针所指向的字符
  while (left < right) {
    let temp = s[left];
    s[left] = s[right];
    s[right] = temp;
    left++;
    right--;
  }
  return s;
};
```
测试用例：
```javascript
console.log(reverseString("hello")); // "olleh"
console.log(reverseString("abcdefg")); // "gfedcba"
console.log(reverseString("12345")); // "54321"
```
3. 存在重复元素（Contains Duplicate）
题目描述：
给定一个整数数组，判断是否存在重复元素。如果存在一值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
示例：
```javascript
输入: [1,2,3,1]
输出: true
```
解答：
```javascript
const containsDuplicate = function(nums) {
  const set = new Set();
  // 遍历数组，使用 Set 来判断是否存在重复元素
  for (let num of nums) {
    if (set.has(num)) {
      return true;
    }
    set.add(num);
  }
  return false;
};
```
测试用例：
```javascript
console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true
```
以上是三道 LeetCode 简单难度的题目和用 JavaScript 编写的代码解答以及测试用例。希望对你有帮助！