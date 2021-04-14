import cat from './scottish_fold.jpeg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>The Cat of the Day</p>
        <img src={cat} className="App-cat" alt="Scottish fold cat" />
        <br/>
        <a
          className="App-link"
          href="https://thecatapi.com/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Scottish fold from The Cat API
        </a>
      </header>
    </div>
  );
}

export default App;
