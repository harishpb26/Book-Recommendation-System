import React, { useEffect, useState } from 'react';
import '../App.css';
import Lists from "./Lists"

let index = 0;
const size = 5;
function Books() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        fetch("/books", {
            method: "POST",
            headers: { "Content-Type": "application/json",
            },
            body: JSON.stringify({index, size}),
        }).then((response) =>
        response.json().then((data) => {
            if(data.books !== ""){
                setBooks(data.books);
                console.log(data.books);
                console.log(data.books.length);
                console.log("index before", index);
                index = index + size;
                console.log("index", index);
            }
      })
    );
    }, [books]);

    return (
    <div>
        <Lists books = {books} />
    </div>
  );
}

export default Books;
