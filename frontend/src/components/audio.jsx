import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import {useState} from 'react'
import { FaMicrophoneAlt } from "react-icons/fa";
import NavBar from './navbar';
import Footer from './footer';

import {
    VStack, 
    Text,
    Button,
    Container,
    Stack,
    Icon
} from "@chakra-ui/react";

const Audio = () => {
    const [recordState, setRecordState] = useState(null); 
    const [audioData, setAudioData] = useState(null); 
    const start = () => {
        setRecordState(RecordState.START); 
    }

    const stop = () => {
        setRecordState(RecordState.STOP);
    }

    const onStop = (data) => {
        setAudioData(data); 
        console.log(audioData); 
    }

    const pause = () => {
        setRecordState(RecordState.PAUSE); 
    }

    return (
        <>
        <NavBar />
        <Container maxWidth="container.xl" bg='blue.600' spacing="14px" centerContent padding={20}>
            <VStack spacing="25px"> 
                <VStack>
                    <Icon as={FaMicrophoneAlt} w={20} h={20} />
                </VStack>
                <VStack>
                    <AudioReactRecorder
                        state={recordState}
                        onStop={onStop}
                        backgroundColor='rgba(66, 153, 225, 0.6)'
                        canvasHeight={100}
                    />
                </VStack>
                
                <VStack>
                    <audio
                    id='audio'
                    controls
                    src={audioData ? audioData.url : null}
                    ></audio>
                </VStack>

                <Stack direction="row" spacing={4}>
                    <Button colorScheme='teal' onClick={start}>Start</Button>
                    <Button colorScheme='orange' onClick={pause}>Pause</Button>
                    <Button colorScheme='red' onClick={stop}>Stop</Button>
                </Stack>
            </VStack>
        </Container>
        <Footer />
        </>
    )
}
export default Audio; 