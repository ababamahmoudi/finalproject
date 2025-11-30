import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Products from "./pages/Products";
import ProductDetail from "./pages/ProductDetail";

function Home() {
  return (
    <div style={{ color: "white", padding: "2rem" }}>
      <h1>Welcome to CloudMart</h1>
      <p>Your enterprise cloud e-commerce platform.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div style={{ background: "#111", padding: "1rem", color: "white" }}>
        <Link to="/" style={{ marginRight: "1rem", color: "cyan" }}>Home</Link>
        <Link to="/products" style={{ color: "cyan" }}>Products</Link>
      </div>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
	<Route path="/products/:id" element={<ProductDetail />} />
      </Routes>
    </Router>
  );
}

export default App;

