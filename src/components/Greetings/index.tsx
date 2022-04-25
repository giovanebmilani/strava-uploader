import { Container, Image, Text } from './styles'

export function Greetings() {
  function handleSayHello() {
    window.Main.sendMessage('Hello World');

    console.log('Message sent! Check main process log in terminal.')
  }

  return (
    <Container>
      <h1>STRAVA</h1>
      <Image
        src="https://www.vectorlogo.zone/logos/reactjs/reactjs-icon.svg"
        alt="ReactJS logo"
      />
      <Text>An Electron boilerplate including TypeScript, React, Jest and ESLint.</Text>
    </Container>
  )
}
 
