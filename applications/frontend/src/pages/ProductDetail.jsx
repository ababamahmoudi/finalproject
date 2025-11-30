import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function ProductDetail() {
    const { id } = useParams();
    const apiBase = import.meta.env.VITE_API_URL;

    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch(`${apiBase}/products/${id}`)
            .then(res => res.json())
            .then(data => {
                setProduct(data);
                setLoading(false);
            })
            .catch(err => console.error(err));
    }, [id]);

    if (loading) return <h2 style={{ color: "white" }}>Loading…</h2>;
    if (!product) return <h2 style={{ color: "white" }}>Not found</h2>;

    return (
        <div style={{ padding: "2rem", color: "white" }}>
            <h1>{product.name}</h1>
            <p>{product.description}</p>

            <p><strong>Price:</strong> ${product.price}</p>
            <p><strong>Category:</strong> {product.category}</p>
            {"stock" in product && (
                <p><strong>Stock:</strong> {product.stock}</p>
            )}
        </div>
    );
}

export default ProductDetail;
