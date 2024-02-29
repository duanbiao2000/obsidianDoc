```tsx
//App.tsx
import {useRef} from "react"

function App(){
  const ref = useRef(null)
  return <Child ref={ref} />
}

export default App
```

```tsx
//Child.tsx
import {FC, forwardRef} from 'react'

interface ChildProps {
  ref:React.MutableRefObject<null>
}

const Child: FC<ChildProps> = ({ref})=>{
  console.log(ref.current)
  return <div>Child</div>
}

export default Child
```

```tsx
//main.tsx


```