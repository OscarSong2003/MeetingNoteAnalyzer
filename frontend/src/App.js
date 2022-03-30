import './App.css';
import { Route, Routes, BrowserRouter } from "react-router-dom";
import Audio from "./components/audio";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Audio />} />
      </Routes>
    </BrowserRouter>

  );
}

export default App;