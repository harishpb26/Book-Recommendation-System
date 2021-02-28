import React, { useState } from "react";
import { Form, Input, Rating, Header, Divider } from "semantic-ui-react";

export const BookForm = ({ onBook }) => {
 const [title, setTitle] = useState("");
 const [average_rating, setRating] = useState(1);
 const [authors, setAuthor] = useState("");
 const [addedTitle, setAdd] = useState("");

 return (
     <div style = {{paddingTop: "110px", paddingLeft: "600px" }}>
     <Divider hidden/>
         { addedTitle &&
             <div>
             <Header as='h3' block style = {{width: "600px"}}>
                 Added Book {addedTitle}
             </Header>
             <Divider hidden/>
             </div>
         }
       <Form style = {{width: "600px"}}>
         <Form.Field>
         <label>Title</label>
           <Input
             placeholder="Title"
             value={title}
             onChange={e => setTitle(e.target.value)}
           />
         </Form.Field>
         <Form.Field>
         <label>Author</label>
           <Input
             placeholder="Author"
             value={authors}
             onChange={e => setAuthor(e.target.value)}
           />
         </Form.Field>
         <Form.Field>
         <label>Rating</label>
           <Rating
             icon="star"
             size="massive"
             rating={average_rating}
             maxRating={5}
             onRate={(_, data) => {
               setRating(data.rating);
             }}
           />
         </Form.Field>
         <Form.Field>
           <button className="ui right labeled icon button"
             onClick={async () => {
               const book = { title, authors, average_rating};
               console.log(book);
               await fetch("/add_book", {
                 method: "POST",
                 headers: {
                   "Content-Type": "application/json"
                 },
                 body: JSON.stringify(book)
             })
            .then((response) =>
                  response.json().then((data) => {
                      if(data.books === ""){
                          alert("Title and Author are required");
                          setAdd("");
                          setTitle("");
                          setAuthor("");
                          setRating(1);
                      }
                      else{
                          console.log(data);
                          console.log("Added into db");
                          setAdd(title);
                          setTitle("");
                          setAuthor("");
                          setRating(1);
                      }

                  })
                );
             }}
           >
           <i className="right arrow icon"></i>
             Add
           </button>
         </Form.Field>
       </Form>
   </div>
 );
};

/*
import React from "react";
import { Header, Form, Button, Rating } from "semantic-ui-react";

class Add extends React.Component {
state = {
    rating: 0,
}
  render() {
    return(
        <div style = {{paddingTop: "100px", margin: "0 auto", paddingLeft: "50px"}}>
        <Form>
           <Form.Field>
             <label>Title</label>
             <input placeholder='Title'/>
           </Form.Field>
           <Form.Field>
             <label>Author</label>
             <input placeholder='Author' />
           </Form.Field>
           <Form.Field>
             <label>Author</label>
             <Rating icon='star' maxRating={5} onRate={(_,data) =>{
                 console.log(data);
                 this.setState({rating: data.rating});
                 console.log(this.state.rating);
             }}/>
           </Form.Field>
           <Button type='submit'>Submit</Button>
     </Form>
        </div>
    );
  }
}

export default Add;
*/
