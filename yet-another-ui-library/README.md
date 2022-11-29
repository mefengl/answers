# Yet Another UI Library

Believe in yourself, every front-end developer can write a worse UI library.

## Carousel

https://dev.to/rakumairu/series/10444

```ts
import { useEffect, useState } from "react";

export default function Carousel({ children }) {
  const [length, setLength] = useState(children.length);
  useEffect(() => setLength(children.length), [children]);

  const [current, setCurrent] = useState(0);
  const next = () => current < length - 1 && setCurrent(current + 1)
  const prev = () => current > 0 && setCurrent(current - 1)

  return (
    <div className="relative overflow-hidden">
      {current > 0 && <button onClick={prev} className="left-6 top-1/2 absolute z-10 w-12 h-12 -translate-y-1/2 bg-white border rounded-full" >
        &lt;
      </button>}
      <div className="[&>*]:w-full [&>*]:flex-shrink-0 [&>*]:flex-grow flex transition-all duration-700"
        style={{ transform: `translateX(-${current * 100}%)` }}>
        {children}
      </div>
      {current < length - 1 && <button onClick={next} className="right-6 top-1/2 absolute z-10 w-12 h-12 -translate-y-1/2 bg-white border rounded-full" >
        &gt;
      </button>}
    </div>
  )
};
```
