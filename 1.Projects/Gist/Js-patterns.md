```js
// 1. Module Pattern
export const Counter = (() => {
  let count = 0;
  return {
    increment() { count++; },
    getCount() { return count; }
  };
})();

// 2. Singleton Pattern
export class Singleton {
  private static instance: Singleton;
  private constructor() {}

  static getInstance(): Singleton {
    if (!Singleton.instance) {
      Singleton.instance = new Singleton();
    }
    return Singleton.instance;
  }
}

// 3. Observer Pattern
export type Observer<T> = (data: T) => void;

export class Observable<T> {
  private subscribers: Observer<T>[] = [];

  subscribe(fn: Observer<T>) {
    this.subscribers.push(fn);
  }

  unsubscribe(fn: Observer<T>) {
    this.subscribers = this.subscribers.filter(sub => sub !== fn);
  }

  notify(data: T) {
    this.subscribers.forEach(fn => fn(data));
  }
}

// 4. Registry Pattern
export class Registry<T> {
  private items: Map<string, T> = new Map();

  register(name: string, item: T) {
    this.items.set(name, item);
  }

  get(name: string): T | undefined {
    return this.items.get(name);
  }
}

// 5. Mixin Pattern
export type Constructor<T = {}> = new (...args: any[]) => T;

export function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    timestamp = Date.now();
  };
}

// 6. Proxy Pattern With Proxy Objects
export function createLoggingProxy<T extends object>(target: T): T {
  return new Proxy(target, {
    get(obj, prop: string) {
      console.log(`Accessing property: ${prop}`);
      return obj[prop as keyof T];
    }
  });
}

// 7. Proxying Function Calls
export function proxyFunction<T extends (...args: any[]) => any>(fn: T): T {
  return new Proxy(fn, {
    apply(target, thisArg, args) {
      console.log('Function called with:', args);
      return Reflect.apply(target, thisArg, args);
    }
  });
}

// 8. Implementing Data Binding With Proxy Objects
export function createBinding<T extends object>(obj: T, callback: (prop: keyof T, value: any) => void): T {
  return new Proxy(obj, {
    set(target, prop: string, value) {
      target[prop as keyof T] = value;
      callback(prop as keyof T, value);
      return true;
    }
  });
}

// Example binding usage:
// const data = createBinding({ text: '' }, (prop, value) => {
//   document.querySelector('#output')!.textContent = String(value);
// });

```