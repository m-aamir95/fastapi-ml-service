// Bootstrap CSS
import "bootstrap/dist/css/bootstrap.min.css";
// Bootstrap Bundle JS
import "bootstrap/dist/js/bootstrap.bundle.min";

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'

import infoIcon from './icons/info-icon.svg'

const App = () => {
  return (
    <Container fluid>
      <Row className="mt-5">
        <Col md={9}>
          Hello
        </Col>

        <Col md={3}>
          <Card
            style={{ width: '18rem' }}
            bg="secondary"
            text="light"
          >
            <Card.Body>
              <Card.Title>About the app</Card.Title>
              <Card.Text>
                    The <b>Sentiment Analysis Service</b> is designed for internal utilization as a tool and API.
                    This user interface has been developed solely for demonstrative purposes
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>


      </Row>
      
      <Row className="mt-3">
        <Col md={9}>
        </Col>
        <Col>
          
        <Col md={3}>
          <Card
            style={{ width: '18rem' }}
            bg="success"
            text="light"
          >
            <Card.Body>
              <Card.Title>About the Machine learning model</Card.Title>
              <Card.Text>
                  Our backend system hosts a HuggingFace DistilBERT model that has undergone fine-tuning.
                  This fine-tuned model has been trained on a dataset of Amazon appliance reviews.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        </Col>
      </Row>
    </Container>
  );
};

export default App;