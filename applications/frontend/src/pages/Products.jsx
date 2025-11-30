import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function Products() {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    const apiBase = import.meta.env.VITE_API_URL || "http://localhost:8000";

    useEffect(() => {
        fetch(`${apiBase}/products`)
            .then((res) => res.json())
            .then((data) => {
                setProducts(data);
                setLoading(false);
            })
            .catch((err) => {
                console.error("Error fetching products:", err);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <div style={{ color: "white", padding: "2rem" }}>
                <h2>Products</h2>
                <p>Loading…</p>
            </div>
        );
    }

    return (
        <div style={{ color: "white", padding: "2rem" }}>
            <h2>Products</h2>

            {products.length === 0 && <p>No products found.</p>}

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
                    gap: "1rem",
                }}
            >
                {products.map((p) => (
                    <Link 
                        key={p.id}
                        to={`/products/${p.id}`}
                        style={{ textDecoration: "none", color: "inherit" }}
                    >
                        <div
                            style={{
                                padding: "1rem",
                                background: "#222",
                                borderRadius: "8px",
                                cursor: "pointer",
                                border: "1px solid #444",
                            }}
                        >
                            <h3 style={{ color: "cyan" }}>{p.name}</h3>
                            <p>{p.description}</p>

                            <p style={{ marginTop: "0.5rem" }}>
                                <strong>${p.price.toFixed(2)}</strong>
                            </p>

                            <p style={{ marginTop: "0.3rem" }}>
                                Category: {p.category}
                            </p>

                            {p.sku && (
                                <p style={{ fontSize: "0.9rem", opacity: 0.8 }}>
                                    SKU: {p.sku}
                                </p>
                            )}
                        </div>
                    </Link>
                ))}
            </div>
        </div>
    );
}

export default Products;

console.log("API URL:", import.meta.env.VITE_API_URL);

