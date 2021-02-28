import React from "react";
import Carousel from 'react-bootstrap/Carousel';
import First from "..//lib_shelf.jpg";

class Home extends React.Component {
  render() {
    return(
        <Carousel>
            <Carousel.Item>
                <img
                className=""
                src={First}
                alt="First slide"
                />
            </Carousel.Item>

            <Carousel.Item>
                <img
                className=""
                src={First}
                alt="Second slide"
                />
            </Carousel.Item>

            <Carousel.Item>
                <img
                className=""
                src={First}
                alt="Third slide"
                />
            </Carousel.Item>
        </Carousel>
    );
  }
}

export default Home;
