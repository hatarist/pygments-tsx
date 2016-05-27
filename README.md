pygments-tsx
============

It's just a subclass of the built-in Pygments' `TypeScriptLexer` 
that supports the `*.tsx` file extension.


Install
-------

    python setup.py install

(use `sudo` if needed)


Usage
-----

It should hook to the Pygments library automatically.

```$ pygmentize greeter.tsx```

```typescript
class Greeter {
    constructor(public greeting: string) { }
    greet() {
        return "<h1>" + this.greeting + "</h1>";
    }
};

var greeter = new Greeter("Hello, world!");

document.body.innerHTML = greeter.greet();
```


License
-------
[WTFPL](http://www.wtfpl.net/)
