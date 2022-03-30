import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import {useState} from 'react'
import { FaMicrophoneAlt } from "react-icons/fa";
import {
    VStack, 
    Text,
    Button,
    Container,
    HStack, 
    Flex,
    Center,
    Box,
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
        <Container maxWidth="container.xl" bg='blue.600' spacing="10px" centerContent padding={20}>
            <VStack spacing="25px"> 
                <VStack>
                    <Icon as={FaMicrophoneAlt} w={20} h={20} />
                </VStack>
                <VStack>
                    <AudioReactRecorder
                        state={recordState}
                        onStop={onStop}
                        backgroundColor='rgb(201, 198, 189)'
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
    )
}
export default Audio; 