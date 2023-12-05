const fs = require("fs");

//These variables are injected from docker-compose -> dockerfile -> shell environment
const public_ip = process.env.public_ip || undefined;

const env_file_content = `
REACT_APP_PUBLIC_IP=${public_ip}
`;

//Create a .env file at the root of the reactjs projects that is where the project package.json is located
//Remember there are two package.json files one is used by the create-react-app and other one inside the project
//created by the create-react-app we are interested in the one created inside the project which is generated
//by create-react-app
fs.writeFileSync("../.env", env_file_content);