import React from 'react';
import { List, Header, Rating, Image, Divider } from "semantic-ui-react";

class Recommend extends React.Component {

  render() {
    return(
        <div style = {{paddingTop: "50px"}}>
        <Header as='h3' block>
            Recommended Books for {this.props.title}
        </Header>
        <List style = {{paddingLeft: "150px"}}>
            {this.props.listofbooks.map(book => {
                return (
                    <List.Item>
                        <Header>{book.title}</Header>
                        <Rating rating = {book.average_rating} maxRating = {5} disabled/>
                        <Divider hidden />
                        <Image src={book.image_url} size='small' />
                        <Divider/>
                    </List.Item>
                )
            })}
        </List>
        </div>
    );
  }
}

export default Recommend;
