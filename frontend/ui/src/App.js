// Bootstrap CSS
import "bootstrap/dist/css/bootstrap.min.css";
// Bootstrap Bundle JS
import "bootstrap/dist/js/bootstrap.bundle.min";

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import ProgressBar from 'react-bootstrap/ProgressBar';
import Badge from 'react-bootstrap/Badge';

import { useState, useEffect } from 'react';

const App = () => {

  const defaultSentimentText = "Hello this app is simple but useful";
  const [sentimentText, setSentimentText] = useState(defaultSentimentText);

  const [prevSentimentText, setPrevSentimentText] = useState("");

  useEffect(() => {
    const interval = setInterval(() => {
      if (sentimentText != prevSentimentText) {
        setPrevSentimentText(sentimentText);
        console.log(`${sentimentText}`);
      }
    }, 1000);

    return () => clearInterval(interval);
  });

  return (
    <Container fluid>
      <Row className="mt-5">
        <Col md={1} />



        <Col md={7}>


          <Form className="mt-5">
            <Form.Group className="mb-3" controlId="text_to_classify">
              <Form.Label>Text to classify</Form.Label>
              <Form.Control as="textarea" rows={3} defaultValue={defaultSentimentText} onChange={ (e) => setSentimentText(e.target.value)} />
            </Form.Group>



            {/* <Button variant="info" type="submit">
                  Login
                </Button> */}
          </Form>
        </Col>

        <Col md={1} />


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

      <Row className="mt-2">

        <Col md={1}></Col>

        <Col md={7}>
          <Badge className="mb-2" bg="secondary">Positive Sentiment</Badge>
          <ProgressBar variant="success" now={10} label={`${10}%`} animated />

          <Badge className="mt-3 mb-2" bg="secondary">Negative Sentiment</Badge>
          <ProgressBar variant="danger" now={40} label={`${40}%`} animated />
        </Col>

        <Col md={1}></Col>


        <Col md={3}>
          <Card
            style={{ width: '18rem' }}
            bg="warning"
            text="dark"
          >
            <Card.Body>
              <Card.Title>About the Machine learning model</Card.Title>
              <Card.Text>
                Our backend system hosts a <a href="https://huggingface.co/m-aamir95/finetuning-sentiment-classification-model-with-amazon-appliances-data">HuggingFace DistilBERT model that has undergone fine-tuning</a>.
                This fine-tuned model has been trained on a dataset of Amazon appliance reviews
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row className="mt-2">
        <Col md={1}></Col>
        <Col md={7}></Col>
        <Col md={1}></Col>
        <Col md={3}>
          <Card
            style={{ width: '18rem' }}
            bg="danger"
            text="light"
          >
            <Card.Body>
              <Card.Title>Inner workings and usage</Card.Title>
              <Card.Text>
                Internally, the system keeps track of all text classification requests, maintaining a record of each one.
                It also employs a straightforward authentication mechanism to manage and monitor user interactions
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default App;