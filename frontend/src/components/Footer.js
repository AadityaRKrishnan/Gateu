import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
function Footer(){
    const d = new Date();
    let year = d.getFullYear();
    return (
        <footer>
            <Container>
            <Row>
                <Col className='text-center py-3'>
                Copyright &copy; Gateau {year}
                </Col>
            </Row>

            </Container>
        </footer>
    )
}

export default Footer