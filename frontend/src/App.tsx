import {
  ChakraProvider,
  Box,
  VStack,
  Grid,
  theme,
} from "@chakra-ui/react";
import { ColorModeSwitcher } from "./ColorModeSwitcher";
import { AddDocument } from "./components/AddDocument";
import { ListAnswers } from "./components/ListDocument";


export const App = () => {

  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center" fontSize="xl">
        <Grid minH="100vh" p={3}>
          <ColorModeSwitcher justifySelf="flex-end" />
          <VStack spacing={8}>
            <AddDocument />
            <ListAnswers />
          </VStack>
        </Grid>
      </Box>
    </ChakraProvider>
  )

}
