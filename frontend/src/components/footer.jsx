import { ButtonGroup, Container, IconButton, Stack, Text } from '@chakra-ui/react'
import react from 'react'
import { FaGithub, FaLinkedin, FaTwitter } from 'react-icons/fa'
import { Logo } from './logo'

const Footer = () => (
    <Container as="footer" role="contentinfo" py={{ base: '12', md: '16' }}>
      <Stack spacing={{ base: '4', md: '5' }}>
        <Stack justify="space-between" direction="row" align="center">
          <Logo />
          <ButtonGroup variant="ghost">
            <IconButton
              as="a"
              href="https://www.linkedin.com/in/linfeng-oscar-song-b56877186/"
              aria-label="LinkedIn"
              icon={<FaLinkedin fontSize="1.25rem" />}
            />
            <IconButton as="a" href="https://github.com/OscarSong2003/MeetingNoteAnalyzer.git" aria-label="GitHub" icon={<FaGithub fontSize="1.25rem" />} />
          </ButtonGroup>
        </Stack>
        <Text fontSize="sm" color="subtle">
          &copy; {new Date().getFullYear()} 
        </Text>
      </Stack>
    </Container>
  )

export default Footer;

