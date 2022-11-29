# Yet Another UI Library

Believe in yourself, every front-end developer can write a worse UI library.

## Carousel

https://dev.to/rakumairu/series/10444

```ts
import { Children, useEffect, useState } from "react";

export default function Carousel({ children }) {
  const [length, setLength] = useState(Children.count(children));
  useEffect(() => setLength(Children.count(children)), [children]);

  const [current, setCurrent] = useState(0);
  const next = () => current < length - 1 && setCurrent(current + 1)
  const prev = () => current > 0 && setCurrent(current - 1)

  return (
    <div className="relative overflow-hidden">
      {current > 0 && <button onClick={prev} className="left-6 top-1/2 absolute z-10 -translate-y-1/2" >
        &lt;
      </button>}
      <div className="flex transition-all duration-700"
        style={{ transform: `translateX(-${current * 100}%)` }}>
        {Children.toArray(children).map((child, index) => (
          <div key={index} className="place-items-center grid flex-grow flex-shrink-0 w-full">
            {child}
          </div>
        ))}
      </div>
      {current < length - 1 && <button onClick={next} className="right-6 top-1/2 absolute z-10 -translate-y-1/2" >
        &gt;
      </button>}
    </div>
  )
};
```
