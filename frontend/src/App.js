import './App.css';
import { Route, Routes, BrowserRouter } from "react-router-dom";
import Audio from "./components/audio";
import 'bootstrap/dist/css/bootstrap.min.css';
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