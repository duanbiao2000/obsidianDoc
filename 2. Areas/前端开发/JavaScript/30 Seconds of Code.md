[30 seconds of code](https://www.30secondsofcode.org/)

```js
// Statements
let x = 0;
function add(a, b) { return a + b; }
if (true) { console.log('Hi'); }

// Expressions
x;          // Resolves to 0
3 + x;      // Resolves to 3
add(1, 2);  // Resolves to 3
```

### undeclared

A variable is undeclared if it has not been declared with an appropriate keyword (i.e. `var`, `let` or `const`). Accessing an undeclared variable will throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError).

```js
console.log(x); // ReferenceError: x is not defined
```

### undefined

A variable is `undefined` if it hasn't been assigned a value. `undefined` is a primitive data type in JavaScript and represents the absence of a value, intentional or otherwise.

```js
let x;
console.log(x); // undefined
```

### null

A variable is assigned a value of `null` like any other value. `null` is also primitive data type in JavaScript and always represents the intentional absence of a value.

```js
let x = null;
console.log(x); // null
```

### Scope

Variables declared with `var` are function scoped, in contrast to variables declared with `let` or `const` which are block scoped.

```js
const scopeExample = () => {
  var a = 'var';
  let b = 'let';
  console.log(a, b); // 'var', 'let'

  {
    var c = 'var';
    let d = 'let';
    console.log(c, d); // 'var', 'let'
  }

  console.log(c); // 'var'
  console.log(d); // Throws a ReferenceError
};
```

If you want to learn more, we have [an article covering JavaScript variables and scopes in more depth](https://www.30secondsofcode.org/js/s/variable-scope).

### Hoisting

While variables declared with `var` are hoisted to the enclosing scope, variables declared with `let` or `const` are not initialized until their definition is evaluated.

```js
const hoistingExample = () => {
  console.log(a); // undefined
  var a = 'var';
  console.log(a); // 'var'

  console.log(b); // ReferenceError
  let b = 'let';
  console.log(b); // 'let'
};
```

If you want to learn more, we have [an article covering JavaScript hoisting in more depth](https://www.30secondsofcode.org/js/s/variable-hoisting).

### Global object property

At the top level, variables declared with `var`, unlike ones declared with `let` or `const`, create a property on the global object.

```js
var a = 'var';
let b = 'let';

console.log(window.a); // 'var'
console.log(window.b); // undefined
```

### Redeclaration

In strict mode, variables declared with `var` can be re-declared in the same scope, whereas this is not allowed for variables declared with `let` or `const`.

```js
'use strict';
var a = 'var1';
var a = 'var2';

let b = 'let1';
let b = 'let2'; // SyntaxError
```

If you want to learn more, we have [an article covering JavaScript's strict mode in more depth](https://www.30secondsofcode.org/js/s/use-strict).

There are 6 values that are considered **falsy** in JavaScript:

-   The keyword `false`
-   The primitive value `undefined`
-   The primitive value `null`
-   The empty string (`''`, `""`)
-   The global property `NaN`
-   A number or BigInt representing `0` (`0`, `-0`, `0.0`, `-0.0`, `0n`)

Every other value is considered **truthy**. It's important to remember that this applies to all JavaScript values, even ones that might seem falsy, such as empty arrays (`[]`) or empty objects (`{}`).

You can check a value's truthiness using either the `Boolean()` function or a double negation (`!!`).

```js
Boolean(false);         // false
Boolean(undefined);     // false
Boolean(null);          // false
Boolean('');            // false
Boolean(NaN);           // false
Boolean(0);             // false
Boolean(-0);            // false
Boolean(0n);            // false

Boolean(true);          // true
Boolean('hi');          // true
Boolean(1);             // true
Boolean([]);            // true
Boolean([0]);           // true
Boolean([1]);           // true
Boolean({});            // true
Boolean({ a: 1 });      // true
```

### Optional chaining

The [optional chaining operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) (`?.`) allows us to access deeply nested object properties without having to validate each reference in the nesting chain. In case of a reference being nullish (`null` or `undefined`) the optional chaining operator will short-circuit, returning `undefined`. The optional chaining operator can also be used with function calls, returning `undefined` if the given function does not exist.

The resulting code is shorter and simpler, as you can see below:

```js
const data = getDataFromMyAPI();

// Without optional chaining
const userName = data && data.user && data.user.name;
const userType = data && data.user && data.user.type;
data && data.showNotifications && data.showNotifications();

// With optional chaining
const userName = data?.user?.name;
const userType = data?.user?.type;
data.showNotifications?.();
```

### Nullish coalescing

In the same spirit, the [nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator) (`??`) is a logical operator that allows us to check for nullish (`null` or `undefined`) values, returning the right-hand side operand when the value is non-nullish, otherwise returning the left-hand side operand.

Apart from cleaner code, this operator might spare us some headaches related to falsy values:

```js
const config = getServerConfig();

// Without nullish coalescing
const port = config.server.port || 8888;
// Oops! This will be true even if we pass it false
const wrongkeepAlive = config.server.keepAlive || true;
// We'll have to explicitly check for nullish values
const keepAlive =
  (config.server.keepAlive !== null & config.server.keepAlive !== undefined)
  ? config.server.keepAlive : true;

// With nullish coalescing
const port = config.server.port ?? 8888;
// This works correctly
const keepAlive = config.server.keepAlive ?? true;
```

**Note:** Keep in mind that both features are quite new, so their support might not be great just yet (around 80% at the time of writing [[1\]](https://caniuse.com/#feat=mdn-javascript_operators_optional_chaining)[[2\]](https://caniuse.com/#feat=mdn-javascript_operators_nullish_coalescing)).

First of all, any falsy values should be considered blank. These include `null`, `undefined`, `0`, `false`, `''`, and `NaN`.

```js
const isFalsy = value => !value;

isFalsy(null); // true
isFalsy(undefined); // true
isFalsy(0); // true
isFalsy(false); // true
isFalsy(''); // true
isFalsy(NaN); // true
```

Secondly, empty arrays and objects should also be considered blank. This can be easily checked by using [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) for both types of values.

```js
const isEmptyCollection = value =>
  (Array.isArray(value) || value === Object(value)) &&
  !Object.keys(value).length;

isEmptyCollection([]); // true
isEmptyCollection({}); // true
```

In addition to the empty string (`''`), whitespace-only strings should be considered blank, too. A regular expression can be used to check for this.

```js
const isWhitespaceString = value =>
  typeof value === 'string' && /^\s*$/.test(value);

isWhitespaceString(' '); // true
isWhitespaceString('\t\n\r'); // true
```

Finally, we can check for some commonly-used built-in objects. Invalid [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) instances, as well as empty [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) and [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instances should all be considered blank.

```js
const isInvalidDate = value =>
  value instanceof Date && Number.isNaN(value.getTime());
const isEmptySet = value => value instanceof Set && value.size === 0;
const isEmptyMap = value => value instanceof Map && value.size === 0;

isInvalidDate(new Date('hello')); // true
isEmptySet(new Set()); // true
isEmptyMap(new Map()); // true
```

Putting everything together, we can finally set up our `isBlank` method.

```js
const isFalsy = value => !value;
const isWhitespaceString = value =>
  typeof value === 'string' && /^\s*$/.test(value);
const isEmptyCollection = value =>
  (Array.isArray(value) || value === Object(value)) &&
  !Object.keys(value).length;
const isInvalidDate = value =>
  value instanceof Date && Number.isNaN(value.getTime());
const isEmptySet = value => value instanceof Set && value.size === 0;
const isEmptyMap = value => value instanceof Map && value.size === 0;

const isBlank = value => {
  if (isFalsy(value)) return true;
  if (isWhitespaceString(value)) return true;
  if (isEmptyCollection(value)) return true;
  if (isInvalidDate(value)) return true;
  if (isEmptySet(value)) return true;
  if (isEmptyMap(value)) return true;
  return false;
};

isBlank(null); // true
isBlank(undefined); // true
isBlank(0); // true
isBlank(false); // true
isBlank(''); // true
isBlank(' \r\n '); // true
isBlank(NaN); // true
isBlank([]); // true
isBlank({}); // true
isBlank(new Date('hello')); // true
isBlank(new Set()); // true
isBlank(new Map()); // true



```

JavaScript provides two operators for typechecking:

-   [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) is used to typecheck for primitive values
-   `instanceof` is used to typecheck for class instances

Primitive values can't leverage the `instanceof` operator, which is a bit of a letdown. To make matters worse, JavaScript's built-in objects such as [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean), [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) and [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) can only be used with `instanceof` to check for instances created using the corresponding constructor. Moreover, [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) has a few quirks that further complicate matters, such as `typeof null` returning `'object'`.

Yet, there's still hope to use `instanceof` for primitive values. [`Symbol.hasInstance`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance) allows us to customize the behavior of the `instanceof` operator. But, in order to do that, we need to define a `class` for each primitive type. Here's what this looks like:

```js
class PrimitiveNumber {
  static [Symbol.hasInstance] = x  => typeof x === 'number';
}
123 instanceof PrimitiveNumber; // true

class PrimitiveString {
  static [Symbol.hasInstance] = x => typeof x === 'string';
}
'abc' instanceof PrimitiveString; // true

class PrimitiveBoolean {
  static [Symbol.hasInstance] = x => typeof x === 'boolean';
}
false instanceof PrimitiveBoolean; // true

class PrimitiveSymbol {
  static [Symbol.hasInstance] = x => typeof x === 'symbol';
}
Symbol.iterator instanceof PrimitiveSymbol; // true

class PrimitiveNull {
  static [Symbol.hasInstance] = x => x === null;
}
null instanceof PrimitiveNull; // true

class PrimitiveUndefined {
  static [Symbol.hasInstance] = x => x === undefined;
}
undefined instanceof PrimitiveUndefined; // true
```

To determine if a JavaScript object is an array, you can either use [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) or the `instanceof` operator. While both methods work for arrays created either using the array literal syntax or the [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) constructor, there's a key difference. [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) is more reliable, as it works with cross-realm-objects, such as those created in an `iframe`.

```
var iframeEl = document.createElement('iframe');
document.body.appendChild(iframeEl);
iframeArray = window.frames[window.frames.length - 1].Array;

var array1 = new Array(1,1,1,1);
var array2 = new iframeArray(1,1,1,1);

console.log(array1 instanceof Array);   // true
console.log(Array.isArray(array1));     // true

console.log(array2 instanceof Array);   // false
console.log(Array.isArray(array2));     // true
```

As illustrated in the previous example, `instanceof` breaks when working with an `iframe`. However, [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) produces the correct result regardless of the way the array was instantiated.

If you are interested in knowing why `instanceof Array` doesn't work across different globals (i.e. `iframe` or `window`), you can read more about it [here](http://web.mit.edu/jwalden/www/isArray.html).



JavaScript ES6 introduced, among many other things, the [spread operator (`...`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax), which allows an iterable to be expanded in places where zero or more arguments or elements are expected.

We can use the spread operator to convert iterables or, as they are sometimes referred to, array-likes. Let's take a look at some examples:

### String

When the spread operator is applied to a string, the result is an array of strings each one representing a character of the original string:

```
const name = 'Zelda';
const letters = [...name]; // 'Z', 'e', 'l', 'd', 'a'
```

### Set

A [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) is a collection of unique values. When the spread operator is applied to it, the result is an array of the stored values:

```
const data = [1, 2, 3, 1, 2, 4]
const values = new Set(data);
const uniqueValues = [...values]; // [1, 2, 3, 4]
```

Note that the above example is the basis for the [uniqueElements snippet](https://www.30secondsofcode.org/js/s/unique-elements).

### NodeList

A [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) is a collection of nodes, returned by methods such as `Document.childNodes()` or [`Document.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll). While it implements some methods that help manipulate it as an array (e.g. `NodeList.prototype.forEach()`), it's oftentimes desirable to convert it to an array. When the spread operator is applied to it, the result is an array of the contained nodes:

```
const nodes = document.childNodes;
const nodeArray = [...nodes]; // [ <!DOCTYPE html>, html ]
```

# URL parameters as object

JavaScript, Browser, String, Regexp · Oct 22, 2020

Creates an object containing the parameters of the current URL.

-   Use [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match) with an appropriate regular expression to get all key-value pairs.
-   Use [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) to map and combine them into a single object.
-   Pass `location.search` as the argument to apply to the current `url`.

```js
const getURLParameters = url =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf('='))] = v.slice(v.indexOf('=') + 1)), a
    ),
    {}
  );
getURLParameters('google.com'); // {}
getURLParameters('http://url.com/page?name=Adam&surname=Smith');
// {name: 'Adam', surname: 'Smith'}



```

# How do I use JavaScript to modify the URL without reloading the page?

JavaScript, Browser · Sep 27, 2021

![img](https://www.30secondsofcode.org/assets/cover/compass.jpg)

### Using the History API

The HTML5 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) is definitely the way to go for modern websites. It accomplishes the task at hand, while also providing additional functionality. You can use either `history.pushState()` or `history.replaceState()` to modify the URL in the browser, depending on your needs:

```js
// Current URL: https://my-website.com/page_a
const nextURL = 'https://my-website.com/page_b';
const nextTitle = 'My new page title';
const nextState = { additionalInformation: 'Updated the URL with JS' };

// This will create a new entry in the browser's history, without reloading
window.history.pushState(nextState, nextTitle, nextURL);

// This will replace the current entry in the browser's history, without reloading
window.history.replaceState(nextState, nextTitle, nextURL);
```

The arguments for both methods are the same, allowing you to pass a customized serializable `state` object as the first argument, a customized `title` (although most browsers will ignore this parameter) and the `URL` you want to add/replace in the browser's history. Bear in mind that the History API only allows same-origin URLs, so you cannot navigate to an entirely different website.

### Using the Location API

The older [Location API](https://developer.mozilla.org/en-US/docs/Web/API/Location) is not the best tool for the job. It reloads the page, but still allows you to modify the current URL and might be useful when working with legacy browsers. You can modify the URL, using either `Window.location.href`, `location.assign()` or `location.replace()`:

```js
// Current URL: https://my-website.com/page_a
const nextURL = 'https://my-website.com/page_b';

// This will create a new entry in the browser's history, reloading afterwards
window.location.href = nextURL;

// This will replace the current entry in the browser's history, reloading afterwards
window.location.assign(nextURL);

// This will replace the current entry in the browser's history, reloading afterwards
window.location.replace(nextURL);
```

As you can see, all three options will cause a page reload, which can be undesirable. Unlike the History API, you can only set the URL, without any additional arguments.  
Finally, the Location API doesn't restrict you to same-origin URLs, which can cause security issues if you are not careful.



# Understanding the "this" keyword in JavaScript

JavaScript, Function, Object · Jun 12, 2021

![img](https://www.30secondsofcode.org/assets/cover/u-got-this.jpg)

### What is `this`?

In JavaScript, the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) keyword refers to the object that is currently executing the code. The short version of what [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) evaluates to is as follows:

-   By default, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the global object.
-   In a function, when not in strict mode, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the global object.
-   In a function, when in strict mode, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) is `undefined`.
-   In an arrow function, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) retains the value of the enclosing lexical context's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this).
-   In an object method, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the object the method was called on.
-   In a constructor call, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) is bound to the new object being constructed.
-   In an event handler, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) is bound to the element on which the listener is placed.

### Global context

In the global execution context, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the global object.

```
console.log(this === window); // true
```

### Function context

When not in strict mode, a function's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the global object.

```
function f() {
  return this;
}

console.log(f() === window); // true
```

When in strict mode, a function's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) will be `undefined` if not set when entering the execution context.

```
'use strict';

function f() {
  return this;
}

console.log(f()); // undefined
```

### Object context

When a function is called as a method of an object, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the object the method is called on. This applies to methods defined anywhere in the object's prototype chain (i.e. own and inherited methods).

```
const obj = {
  f: function() {
    return this;
  }
};

const myObj = Object.create(obj);
myObj.foo = 1;

console.log(myObj.f()); // { foo: 1 }
```

Similarly, when used inside a constructor, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the object being constructed.

```
class C {
  constructor() {
    this.x = 10;
  }
}

const obj = new C();
console.log(obj.x); // 10
```

### Arrow function context

In arrow functions, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) retains the value of the enclosing lexical context's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this).

```
const f = () => this;

console.log(f() === window); // true

const obj = {
  foo: function() {
    const baz = () => this;
    return baz();
  },
  bar: () => this
};

console.log(obj.foo()); // { foo, bar }
console.log(obj.bar() === window); // true
```

Notice how in the second example, an arrow function's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the global object unless wrapped inside a regular `function` call, whose [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the object it's called from and its lexical context is retained by the arrow function.

### Event handler context

When used in an event handler, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) refers to the element on which the listener is placed.

```
const el = document.getElementById('my-el');

el.addEventListener('click', function() {
  console.log(this === el); // true
});
```

### Binding `this`

Using [`Function.prototype.bind()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) returns a new function from an existing one, where [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) is permanently bound to the first argument of `bind()`.

```
function f() {
  return this.foo;
}

var x = f.bind({foo: 'hello'});
console.log(x()); // 'hello'
```

Similarly, using [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) or [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply) will bind the called function's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) to the first argument of either of these functions only for this call.

```
function f() {
  return this.foo;
}

console.log(f.call({foo: 'hi'})); // 'hi'


```



# Can I use an arrow function as the callback for an event listener in JavaScript?

JavaScript, Browser, Event, Function · Jun 12, 2021

![img](https://www.30secondsofcode.org/assets/cover/coffee-float.jpg)

### Arrow functions

JavaScript ES6 introduced the concept of arrow functions, a new way to define and write functions. While they might seem like a syntactic sugar on top of regular functions, they have a key difference which lies in the way the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) context is bound. I strongly suggest you read [Understanding the "this" keyword in JavaScript](https://www.30secondsofcode.org/blog/s/javascript-this), as I will not go into detail about the topic in this article. To summarize:

>   Arrow functions do not have their own bindings for [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this), resulting in [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) retaining the value of the enclosing lexical context's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this).

### Event listener callbacks

A common task when writing browser-side JavaScript is creating event listeners. For example:

```js
const toggleElements = document.querySelectorAll('.toggle');
toggleElements.forEach(el => {
  el.addEventListener('click', function() {
    this.classList.toggle('active');
  });
});
```

In the example above, we use `NodeList.prototype.forEach()` to iterate over matching nodes and `EventTarget.addEventListener()` with a regular function as the callback for the `'click'` event to swap between an active and inactive state for the clicked element. We are using a regular function, so the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) context inside the callback will be bound to the event target.

### Arrow functions as callbacks

As we have already explained, arrow functions do not have their own bindings for [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this). So what happens if we convert the previous code snippet's callback to an arrow function? Its [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) context refers to the global one, which in this case is the `Window` object.

```js
const toggleElements = document.querySelectorAll('.toggle');
toggleElements.forEach(el => {
  el.addEventListener('click', () => {
    this.classList.toggle('active'); // `this` refers to `Window`
    // Error: Cannot read property 'toggle' of undefined
  });
});
```

This code will fire the event listener and execute the callback anytime the matching element is clicked. It will, however, throw an error, due to the `Window` object not having a `classList` property. Oftentimes, the code could even fail silently. An example would be a condition that always evaluates to `false` for `Window`, but could evaluate to `true` for a given element. Issues like that result in many headaches and wasted hours until you can uncover and fix them.

To deal with this, one could simply use the first argument of the callback function and `Event.target` or `Event.currentTarget` depending on their needs:

```js
const toggleElements = document.querySelectorAll('.toggle');
toggleElements.forEach(el => {
  el.addEventListener('click', (e) => {
    e.currentTarget.classList.toggle('active'); // works correctly
  });
});
```

# Understanding higher-order functions in JavaScript

JavaScript, Function · Nov 7, 2021

![img](https://www.30secondsofcode.org/assets/cover/rock-climbing.jpg)

Higher-order functions are **functions that operate on other functions**, either by accepting them as arguments or by returning them as their results. This allows us to create an abstraction layer over actions, not just values.

The reason we can write higher-order functions in JavaScript is due to the fact that functions are values. This means they can be assigned to variables and passed as values. You might also often hear the term *callback* when referring to a function that is passed as an argument. This is due to it being called by the higher-order function. Callbacks are particularly common in JavaScript, with event handling, asynchronous code and array operations relying heavily on them.

The main advantages of this technique are abstraction, composition, code reusability and readability. Most of the 30 seconds of code snippets are built with higher-order functions in mind. They are small, easily digestible functions that are **highly reusable** and **can be composed** to create more complex logic.

That being said, we can take a look at an example, utilizing some very simple functions:

```
const add = (a, b) => a + b;
const isEven = num => num % 2 === 0;

const data = [2, 3, 1, 5, 4, 6];

const evenValues = data.filter(isEven); // [2, 4, 6]
const evenSum = data.filter(isEven).reduce(add); // 12
```

In this example, we define two simple functions that we then use as callbacks in [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) and [`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) to get the result we want. Both of these functions are higher-order functions. This allows us to create an **abstraction layer for any action** we might want to perform without having to rewrite how the filtering or reduction algorithm is to be applied every single time.

# What are the differences between arrow functions and regular functions in JavaScript?

JavaScript, Function · Oct 17, 2021

![img](https://www.30secondsofcode.org/assets/cover/fallen-leaves.jpg)

JavaScript's arrow functions might seem the same as regular functions on the surface, but they have some very important differences:

-   Syntactical differences
-   [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) value (execution context)
-   Usage as methods
-   Usage as constructors
-   `arguments` binding

### Syntax

The first and most obvious difference between arrow functions and regular functions is their syntax. Not only do they look different, but arrow functions also provide an implicit return shorthand and allow parenthesis around a single argument to be omitted.

```js
const square = a => a * a;

// Equivalent regular function
function square(a) {
  return a * a;
}
```

### Execution context

Inside a regular function, execution context (i.e. the value of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)) is dynamic. This means that the value of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) depends on how the function was invoked (simple invocation, method invocation, indirect invocation or constructor invocation). On the other hand, an arrow function does not define its own execution context. This results in an arrow function's [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) being resolved lexically (i.e. the scope in which the arrow function was defined).

```js
function logThis() {
  console.log(this);
}
document.addEventListener('click', logThis);
// `this` refers to the document

const logThisArrow = () => {
  console.log(this);
};
document.addEventListener('click', logThisArrow);
// `this` refers to the global object
```

[`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call), [`Function.prototype.bind()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) and [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply) do not work correctly with arrow functions either. Their purpose is to allow methods to execute within different scopes, but the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) value of an arrow function cannot be changed, as it's resolved lexically.

```js
function logThis() {
  console.log(this);
}
logThis.call(42);       // Logs: 42

const logThisArrow = () => {
  console.log(this);
};
logThisArrow.call(42);  // Logs the global object
```

### Methods

Due to arrow functions not defining their own execution context, they're not well-suited for usage as methods. However, thanks to the [Class fields proposal](https://github.com/tc39/proposal-class-fields), arrow functions can be used as methods inside classes, if your environment supports it.

```js
const obj = {
  x: 42,
  logThisX: function() {
    console.log(this.x, this);
  },
  logThisXArrow: () => {
    console.log(this.x, this);
  }
};

obj.logThisX();       // Logs: 42, Object {...}
obj.logThisXArrow();  // Logs: undefined, the global object
```

### Constructors

Regular functions can be used as constructors, using the `new` keyword. Yet another consequence of the lexical resolution of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) inside arrow functions is that they cannot be used as constructors. Using `new` with an arrow function results in a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError).

```js
function Foo(bar) {
  this.bar = bar;
}
const a = new Foo(42);  // Foo {bar: 42}

const Bar = foo => {
  this.foo = foo;
};
const b = new Bar(42);  // TypeError: Bar is not a constructor
```

### Arguments

Another difference is the binding of the `arguments` object. Unlike regular functions, arrow functions don't have their own `arguments` object. A modern alternative that circumvents this limitation is the usage of rest parameters.

```js
function sum() {
  return arguments[0] + arguments[1];
};
sum(4, 6);        // 10

const arguments = [1, 2, 3];
const sumArrow = () => {
  return arguments[0] + arguments[1];
};
sumArrow(4, 6);   // 3 (resolves to 1 + 2)

const sumRest = (...arguments) => {
  return arguments[0] + arguments[1];
}
sumRest(4, 6);    // 10
```

### Other differences

Finally, there are a couple of other differences that are not as important, but worth mentioning. These include the lack of a `prototype` property in arrow functions, as well as the fact that the [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield) keyword may not be used in an arrow function's body. A consequence of the latter is that arrow functions cannot be used as generators.

# What is the difference between synchronous and asynchronous code in JavaScript?

JavaScript, Function, Promise · Nov 14, 2021

Synchronous code runs in sequence. This means that each operation must wait for the previous one to complete before executing.

```js
console.log('One');
console.log('Two');
console.log('Three');
// LOGS: 'One', 'Two', 'Three'
```

==Asynchronous code runs in parallel.== This means that an operation can occur while another one is still being processed.
<!--SR:!2023-07-26,6,230-->

```js
console.log('One');
setTimeout(() => console.log('Two'), 100);
console.log('Three');
// LOGS: 'One', 'Three', 'Two'
```

Asynchronous code execution is often preferable in situations where execution can be blocked indefinitely. Some examples of this are ==network requests, long-running calculations, file system operations etc.== 
Using asynchronous code in the browser ensures the page remains responsive and the user experience is mostly unaffected.
<!--SR:!2023-07-17,1,230-->

# Asynchronous JavaScript Cheat Sheet

JavaScript, Function, Promise · Jun 12, 2021

### Promise basics

-   **Promises** start in a **pending state**, neither fulfilled or rejected.
-   When the operation is completed, a promise will become **fulfilled with a value**.
-   If the operation fails, a promise will get **rejected with an error**.

### Creating promises

-   The function passed to the [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) constructor will execute synchronously.
-   Use `resolve()` or `reject()` to create promises from values.
-   `Promise.resolve(val)` will fulfill the promise with `val`.
-   `Promise.reject(err)` will reject the promise with `err`.
-   If you put a fulfilled promise into a fulfilled promise, they will collapse into one.

```js
// Resolving with a value, rejecting with an error
new Promise((resolve, reject) => {
  performOperation((err, val) => {
    if (err) reject(err);
    else resolve(val);
  });
});

// Resolving without value, no need for reject
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
```

### Handling promises

-   [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) accepts two optional arguments (`onFulfilled`, `onRejected`).
-   [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) will call `onFulfilled` once the promise is fulfilled.
-   [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) will call `onRejected` if the promise is rejected.
-   [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) passes errors through if `onRejected` in undefined.
-   [`Promise.prototype.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) accepts one argument (`onRejected`).
-   [`Promise.prototype.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) behaves like [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) when `onFulfilled` is omitted.
-   [`Promise.prototype.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) passes fulfilled values through.
-   [`Promise.prototype.finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally) accepts one argument (`onFinally`).
-   [`Promise.prototype.finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally) calls `onFinally` with no arguments once any outcome is available.
-   [`Promise.prototype.finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally) passes through input promise.

```js
promisedOperation()
  .then(
    val => value + 1,   // Called once the promise is fulfilled
    err => {            // Called if the promise is rejected
      if (err === someKnownErr) return defaultVal;
      else throw err;
    }
  )
  .catch(
    err => console.log(err); // Called if the promise is rejected
  )
  .finally(
    () => console.log('Done'); // Called once any outcome is available
  );
```

-   All three of the above methods will not be executed at least until the next tick, even for promises that already have an outcome.

### Combining promises

-   [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) turns an array of promises into a promise of an array.
-   If any promise is rejected, the error will pass through.
-   [`Promise.race()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race) passes through the first settled promise.

```js
Promise
  .all([ p1, p2, p3 ])
  .then(([ v1, v2, v3 ]) => {
    // Values always correspond to the order of promises,
    // not the order they resolved in (i.e. v1 corresponds to p1)
  });

Promise
  .race([ p1, p2, p3 ])
  .then(val => {
    // val will take the value of the first resolved promise
  });
```

### async/await

-   Calling an `async` function always results in a promise.
-   `(async () => value)()` will resolve to `value`.
-   `(async () => throw err)()` will reject with an error.
-   `await` waits for a promise to be fulfilled and returns its value.
-   `await` can only be used in `async` functions.
-   `await` also accepts non-promise values.
-   `await` always waits at least until the next tick before resolving, even when waiting already fulfilled promises or non-promise values.

```js
async () => {
  try {
    let val = await promisedValue();
    // Do stuff here
  } catch (err) {
    // Handle error
  }
}
```

# Tip: The order of then and catch matters

JavaScript, Function, Promise · Jun 12, 2021

![img](https://www.30secondsofcode.org/assets/cover/blue-sunrise.jpg)

Many if not most promise-related headaches come from incorrectly ordered [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) and [`Promise.prototype.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) methods. The order in which these methods are chained to a promise can lead to very different behaviors. Let's take a look at a very simple example:

```
const myPromise = () => Promise.reject('Oops!');
const logger = data => console.log(data);
const identity = data => data;

myPromise().catch(identity).then(logger); // LOGS: Oops!
myPromise().then(logger).catch(identity); // Nothing is logged
```

As you can see from this example, swapping the `catch()` and `then()` methods results in entirely different behavior, even though the promise has the same result. This is due to the fact that each chained method will result itself in a promise. This means that the first one will pass its result to the second, the second to the third and so on and so forth. While this might seem obvious when looking at an example like this one, many times it's overlooked and can result in hard to debug issues. This is especially true when the promise chain is long and complicated.

So, next time you are working with promises, try to think of `then()` and `catch()` methods in terms of promise chaining and remember that order matters!

# Where and how can I use memoization in JavaScript?

JavaScript, Function, Memoization · Nov 7, 2021

![img](https://www.30secondsofcode.org/assets/cover/cherry-trees.jpg)

Memoization is a commonly used technique that can help speed up your code significantly. This technique relies on a **cache** to store results for previously completed units of work. The purpose of the cache is to **avoid performing the same work more than once**, speeding up subsequent calls of time-consuming functions. Based on this definition, we can easily extract some criteria that can help us decide when to use memoization in our code:

-   Memoization is useful mainly in speeding up slow-performing, costly or time-consuming function calls
-   Memoization speeds up subsequent calls, so it's best used when you anticipate multiple calls of the same function under the same circumstances
-   Memoization stores results in memory, so it should be avoided when the same function is called multiple times under very different circumstances

A simple, object-oriented example of implementing memoization could be as follows:

```
class MyObject {
  constructor(data) {
    this.data = data;
    this.data[this.data.length - 2] = { value: 'Non-empty' };
  }

  firstNonEmptyItem() {
    return this.data.find(v => !!v.value);
  }

  firstNonEmptyItemMemo() {
    if (!this.firstNonEmpty)
      this.firstNonEmpty = this.data.find(v => !!v.value);
    return this.firstNonEmpty;
  }
}

const myObject = new MyObject(Array(2000).fill({ value: null }));

for (let i = 0; i < 100; i ++)
  myObject.firstNonEmptyItem();       // ~4000ms
for (let i = 0; i < 100; i ++)
  myObject.firstNonEmptyItemMemo();   // ~70ms
```

This example showcases a way to implement memoization inside a class. However, it makes a couple of assumptions. First, it's assumed that the `data` structure will not be altered over the lifecycle of the object. Seconds, it's assumed that this is the only expensive function call we will make, so the code is not reusable. The example also doesn't account for arguments being passed to the function, which would alter the result. A functional approach would work with any given function and also account for arguments. Such an approach can be seen in the form of the [memoize snippet](https://www.30secondsofcode.org/js/s/memoize/), which uses a [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) to store different values.

We still recommend using that snippet as the primary way to memoize a function, however JavaScript's [Proxy object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) provides an interesting alternative via the use of the `handler.apply()` trap, which can be used for this purpose as follows:

```
const memoize = fn => new Proxy(fn, {
  cache: new Map(),
  apply (target, thisArg, argsList) {
    let cacheKey = argsList.toString();
    if(!this.cache.has(cacheKey))
      this.cache.set(cacheKey, target.apply(thisArg, argsList));
    return this.cache.get(cacheKey);
  }
});

const fibonacci = n => (n <= 1 ? 1 : fibonacci(n - 1) + fibonacci(n - 2));
const memoizedFibonacci = memoize(fibonacci);

for (let i = 0; i < 100; i ++)
  fibonacci(30);                      // ~5000ms
for (let i = 0; i < 100; i ++)
  memoizedFibonacci(30);              // ~50ms
```

# Tip: Minimize DOM access

JavaScript, Browser · Jun 12, 2021

DOM operations, including accessing the DOM, are generally slow. This is usually not a problem until you have to perform many DOM operations and your JavaScript application's performance starts to suffer. A very quick trick to increase performance is to store DOM elements or their values in local variables if you plan to access them multiple times.

```js
// This is slow, it accesses the DOM element multiple times
document.querySelector('#my-element').classList.add('my-class');
document.querySelector('#my-element').textContent = 'hello';
document.querySelector('#my-element').hidden = false;

// This is faster, it stores the DOM element in a variable
const myElement = document.querySelector('#my-element');
myElement.classList.add('my-class');
myElement.textContent = 'hello';
myElement.hidden = false;
```

Note that, while this trick may come in handy, it comes with the caveat that if you later remove the DOM element and you still have it stored in a variable, the variable should be set to `null` to avoid potential memory leaks.

