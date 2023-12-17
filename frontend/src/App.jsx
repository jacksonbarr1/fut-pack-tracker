import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import NavBar from "./components/NavBar.jsx";
import MyPacks from "./components/MyPacks.jsx";
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Statistics from "./components/Statistics.jsx";
import Settings from "./components/Settings.jsx";


function App() {

  return (
    <Router>
        <NavBar />
        <Routes>
            <Route path="/packs" element={<MyPacks />} />
            <Route path="/statistics" element={<Statistics />} />
            <Route path="/settings" element={<Settings />} />
        </Routes>
    </Router>
  )
}

export default App
