import React from 'react';
import { List, Header, Rating, Image, Divider, Button } from "semantic-ui-react";
import Recommend from "./Recommend";

class Lists extends React.Component {
    state = {
        listofbooks: [],
        displayRecommended: false,
        displayBooks: true,
        clickedTitle: "",
    }

    constructor(props){
    super(props);
    this.handleClick = this.handleClick.bind(this);
    }

    /*
    handleClick = (e) => {
        console.log(this.props.books);
        fetch("/recommend").then(response =>
        response.json().then(data => {
        console.log(data.books);
        this.setState({listofbooks: data.books, displayRecommended: true, displayBooks: false});
        })
        );
    };
    */

    render() {
    return(
        <div>
        {
            this.state.displayBooks && <List style = {{paddingLeft: "150px", paddingTop: "50px"}}>
                {this.props.books.map(book => {
                    return (
                        <List.Item>
                            <Header>{book.title}</Header>
                            <Rating rating = {book.average_rating} maxRating = {5} disabled/>
                            <Divider hidden />
                            <Button content = "Recommend" onClick = {e =>
                                this.handleClick(book.title)} size = "small"/>
                            <Divider hidden />
                            <Image src={book.image_url} size='small' />
                            <Divider/>
                        </List.Item>
                    )
                })}
            </List>

        }
        {
            this.state.displayRecommended && <Recommend listofbooks = {this.state.listofbooks} title = {this.state.clickedTitle}/>
        }
        </div>
    );
    }
    handleClick(title) {
        console.log(title);
        var recommendTitle = encodeURIComponent(title);
        console.log(recommendTitle);
        fetch("/recommend/" + recommendTitle).then(response =>
            response.json().then(data => {
                console.log(data.books);
                this.setState({listofbooks: data.books, displayRecommended: true, displayBooks: false, clickedTitle: title});
                window.scrollTo(0,0);
            })
        );};
}

export default Lists;
