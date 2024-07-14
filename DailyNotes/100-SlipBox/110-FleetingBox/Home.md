
```jsx
//List.js
import ListItem from './ListItem';
import PropoTypes from 'prop-types';

function List(props) {
  let items = props.items.map(item=><ListItem text={item} />)
  return(
    <>
      <h3>{props.title}</h3>
      <ul>
        {items}
      </ul>
    </>
  );
}

List.defaultProps = {
  items:[]
  background :'primary'
};

List.proptypes = {
  items: PropTypes.arrray.isrequired,
  item: PropTypes.string.isrequired,
  background: PropTypes.oneOf([
    'primary',
    'secondary'
  ]),
  specialProp: PropTypes.shape({
    name:PropTypes.string,
    age: PropTypes.number
  })
};

export default List;
```

```jsx
//App.js
import Navbar from '.Navbar';
import List from './List';


function App(){
  let guitars = ['Strat', 'Les Paul', 'Explorer'];

  return (
    <>
      <Navbar title="CSS and Separating JS and JSX" />
      <div className = "container">
        <List 
          title="Guitars"
          background="danger"
        />
      </div>  
    </>
  );
}

export default App;
```

```jsx
//Counter.js

import {useState} from 'react';

function Counter(props) {
  const [counter,setCounter] = useState(props.startAt);

  setInterval(()=>setCounter(counter + props.countBy),1000);
  return (
      <>
        <p>Start At: {props.startAt}</p>
        <p>Start By: {props.countBy}</p>
        <h4>{counter}</h4>
      </>
    );
  }
  
Counter.defaultProps = {
  startAt: 0,
  countBy: 1
};

export default Counter;
```

```jsx
//App.js
import Navbar from '.Navbar';
import List from './List';


function App(){
  let guitars = ['Strat', 'Les Paul', 'Explorer'];

  return (
    <>
      <Navbar title="CSS and Separating JS and JSX" />
      <div className = "container">
        <List 
          title="Guitars"
          items={guitars}
        />
      </div>  
    </>
  );
}

export default App;
```